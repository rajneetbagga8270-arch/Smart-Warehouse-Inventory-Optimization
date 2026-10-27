from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Warehouse Intelligence", page_icon="📦", layout="wide")
DATA = Path(__file__).parent / "data" / "warehouse_inventory.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA, parse_dates=["date"])
    df["inventory_value_inr"] = df["stock_on_hand"] * df["unit_cost_inr"]
    df["stock_status"] = (df["stock_on_hand"] <= df["reorder_point"]).map(
        {True: "Reorder", False: "Healthy"}
    )
    return df

df = load_data()
st.title("📦 Warehouse Intelligence")
st.caption("Smart Warehouse & Inventory Optimization | FMCG demo project")
st.info("Portfolio demo using synthetic data only; this is not actual ITC data.")

with st.sidebar:
    st.header("Filters")
    wh_options = sorted(df["warehouse"].unique())
    cat_options = sorted(df["category"].unique())
    wh = st.multiselect("Warehouse", wh_options, default=wh_options)
    cats = st.multiselect("Category", cat_options, default=cat_options)
    start, end = st.date_input("Date range", value=(df.date.min().date(), df.date.max().date()))

f = df[df.warehouse.isin(wh) & df.category.isin(cats)]
f = f[(f.date.dt.date >= start) & (f.date.dt.date <= end)]
if f.empty:
    st.warning("No data for these filters.")
    st.stop()

latest_date = f.date.max()
latest = f[f.date == latest_date]
orders = int(latest.units_ordered.sum())
fulfilled = int(latest.units_fulfilled.sum())
fill_rate = 100 * fulfilled / orders if orders else 0
risk = int((latest.stock_on_hand <= latest.reorder_point).sum())
value = float(latest.inventory_value_inr.sum())
delay = float(latest.delivery_delay_days.mean())

a,b,c,d = st.columns(4)
a.metric("Order fulfilment rate", f"{fill_rate:.1f}%")
b.metric("SKUs at/below reorder point", f"{risk:,}")
c.metric("Inventory value", f"₹{value:,.0f}")
d.metric("Average delivery delay", f"{delay:.2f} days")

left, right = st.columns(2)
with left:
    st.subheader("Demand vs fulfilled units")
    trend = f.groupby("date", as_index=False)[["units_ordered","units_fulfilled"]].sum()
    long = trend.melt("date", var_name="measure", value_name="units")
    st.plotly_chart(px.line(long, x="date", y="units", color="measure"), use_container_width=True)
with right:
    st.subheader("Inventory value by warehouse")
    by_wh = latest.groupby("warehouse", as_index=False).inventory_value_inr.sum()
    st.plotly_chart(px.bar(by_wh, x="warehouse", y="inventory_value_inr"), use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Inventory value by category")
    by_cat = latest.groupby("category", as_index=False).inventory_value_inr.sum()
    st.plotly_chart(px.pie(by_cat, names="category", values="inventory_value_inr", hole=.35), use_container_width=True)
with right:
    st.subheader("Delivery delay distribution")
    st.plotly_chart(px.histogram(f, x="delivery_delay_days", nbins=7), use_container_width=True)

st.subheader("Replenishment watchlist")
watch = latest[latest.stock_on_hand <= latest.reorder_point].copy()
watch["estimated_shortfall_units"] = (watch.reorder_point - watch.stock_on_hand).clip(lower=0)
watch = watch[["warehouse","product_id","product_name","stock_on_hand","reorder_point",
               "estimated_shortfall_units","lead_time_days"]].sort_values(
                   "estimated_shortfall_units", ascending=False)
st.dataframe(watch, use_container_width=True, hide_index=True)
st.download_button("Download filtered data", f.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_warehouse_inventory.csv", mime="text/csv")

st.caption("Metric definitions: fulfilment = units fulfilled ÷ units ordered; inventory value = stock on hand × unit cost. Reorder flags are a simple rule-based alert, not an operational recommendation.")
