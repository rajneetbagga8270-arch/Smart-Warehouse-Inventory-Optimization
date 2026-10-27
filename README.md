# Smart Warehouse & Inventory Optimization Dashboard

An interactive warehouse analytics dashboard designed to monitor inventory levels, order fulfilment, replenishment needs, and delivery delays using Python, SQL, Streamlit, and Plotly.

**Target Role:** Graduate Engineer Trainee (GET) — Supply Chain Management & Warehousing  
**Tech Stack:** Python, Pandas, SQL, Streamlit, Plotly

> **Data Disclaimer:** This project uses synthetic FMCG demo data. It does not contain actual ITC data or represent ITC's operational performance.

## Problem Statement

Warehouse teams need to monitor stock levels, inventory value, fulfilment rates, and delivery delays to identify replenishment priorities and improve inventory planning.

## Key Features

- **Interactive Filters:** Filter data by warehouse, product category, and date range.
- **Order Fulfilment:** Monitor the percentage of ordered units successfully fulfilled.
- **Inventory Monitoring:** Track inventory value and SKUs at or below their reorder points.
- **Demand Analysis:** Compare ordered units against fulfilled units over time.
- **Warehouse Comparison:** Analyze inventory value across warehouses and product categories.
- **Delivery Performance:** Monitor average delivery delays.
- **Replenishment Watchlist:** Identify products that may require restocking.
- **Data Export:** Download filtered data for further analysis.

## Technologies Used

- **Python:** Core programming and data processing.
- **Pandas:** Data cleaning, transformation, and analysis.
- **SQL:** Queries for inventory analysis, replenishment priorities, and warehouse performance.
- **Streamlit:** Interactive dashboard interface.
- **Plotly:** Interactive charts and visualizations.

## Project Structure

```text
Smart-Warehouse-Inventory-Optimization/
├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── warehouse_inventory.csv
└── sql/
    └── analysis_queries.sql
```

## Installation and Setup

**Prerequisites:** Python 3.10 or later and pip.

1. Clone the repository:

   ```bash
   git clone https://github.com/rajneetbagga8270-arch/Smart-Warehouse-Inventory-Optimization.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Smart-Warehouse-Inventory-Optimization
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in your terminal.

## Dataset

The project includes simulated FMCG warehouse data covering January–June 2026 across three warehouses. The dataset is intended for demonstration and analytical practice, not for representing real business results.

## SQL Analysis

The `sql/analysis_queries.sql` file contains example queries for examining inventory levels, replenishment requirements, warehouse performance, and unfulfilled demand.

## Resume Description

**Smart Warehouse & Inventory Optimization Dashboard | Python, SQL, Streamlit, Plotly**

- Developed an interactive dashboard to monitor inventory value, order fulfilment, replenishment risk, and delivery delays across three simulated warehouses.
- Used Pandas for data analysis, Plotly for interactive visualizations, and SQL queries to identify replenishment priorities and compare warehouse performance.

## Future Improvements

- Integrate real warehouse management system data.
- Improve reorder-point calculations using demand variability and supplier lead times.
- Add demand forecasting and safety-stock optimization.
- Evaluate business outcomes using validated operational data.

## Limitations

The dataset is synthetic, and the reorder rules are illustrative. The project does not claim actual cost savings or measured improvements in warehouse performance. Real-world deployment would require validated demand forecasts, supplier lead-time data, and business-approved inventory policies.
