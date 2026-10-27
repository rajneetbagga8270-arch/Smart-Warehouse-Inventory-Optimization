# Smart Warehouse & Inventory Optimization Dashboard

**Target role:** Graduate Engineer Trainee — Supply Chain Management & Warehousing  
**Stack:** Python, Pandas, SQL, Streamlit, Plotly

> **Data note:** This project uses synthetic FMCG demo data. It is not ITC data and must not be presented as actual ITC performance.

## Problem statement
A distributor operating three warehouses needs to monitor inventory value, stockout risk, fulfilment and delivery delays so teams can prioritize replenishment.

## Dashboard features
- Filter by warehouse, product category and date range.
- Monitor order fulfilment rate, SKUs at/below reorder point, inventory value and average delivery delay.
- Compare demand with fulfilled units over time.
- Explore inventory value by warehouse and category.
- View a replenishment watchlist and download filtered data.

## Run it
Install Python 3.10+ then, from this folder:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files
- `app.py`: interactive dashboard
- `data/warehouse_inventory.csv`: synthetic data for Jan–Jun 2026
- `sql/analysis_queries.sql`: five example SQL analyses
- `requirements.txt`: required Python packages

## Resume bullet
**Smart Warehouse & Inventory Optimization Dashboard | Python, SQL, Power BI concepts, Streamlit**
- Built an interactive dashboard to track order fulfilment, inventory valuation, reorder risk and delivery delays across three distribution centres using synthetic FMCG data.
- Wrote SQL analyses to identify replenishment priorities, compare warehouse performance and quantify unfulfilled demand.

## Interview explanation
"I created a warehouse analytics dashboard using synthetic FMCG data for three distribution centres. It tracks fulfilment, inventory value, delivery delays and stock at or below a reorder point. I used Pandas to transform the data, Streamlit and Plotly for interactive visualizations, and SQL to analyze replenishment and warehouse performance. In a real deployment, I would validate the reorder policy using demand variability, supplier lead times, safety stock and actual business data."

## Important limitations
The dataset is simulated, the reorder rule is illustrative, and no real cost savings are claimed. For a production model, use validated demand forecasts, supplier lead-time variability, safety stock and business-approved service levels.
