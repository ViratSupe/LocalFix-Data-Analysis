# LocalFix Operations: Data Analysis & BI Dashboard

## Project Overview
LocalFix is a simulated hyperlocal services marketplace (similar to Urban Company or TaskRabbit). This project is an end-to-end data engineering and business intelligence solution designed to track operational bottlenecks, specifically focusing on user and provider cancellation rates across multiple cities.

I built a custom Python pipeline to generate over 10,000 rows of relational mock data, stored it in an SQLite database, and connected it to Power BI to visualize over ₹8.00M in simulated service revenue.

## 🛠️ Tech Stack
* **Data Generation & Scripting:** Python (Pandas, Faker)
* **Database:** SQLite
* **Data Visualization & Modeling:** Power BI, DAX

## 📊 The Dashboard
*(Include a screenshot of your dashboard here! Upload the image to your repo, then replace the link below)*
![LocalFix Dashboard](link_to_your_screenshot_here.png)

## 💡 Key Business Insights
* **Cancellation Bottlenecks:** Built custom DAX measures to compare `User Cancellation Rate` vs. `Provider Cancellation Rate` across specific service categories (e.g., Appliance Repair, Cleaning).
* **Root Cause Analysis:** Visualized exact cancellation reasons to identify platform drop-off points (e.g., "Distance too far" vs. "Found a cheaper alternative").
* **Financial Tracking:** Monitored total booking volume and aggregated service revenue across various city locations using interactive cross-filtering.

## ⚙️ How It Works
1.  `generate_data.py`: A Python script utilizing the Faker library to generate realistic, interconnected tables for Users, Providers, and Bookings.
2.  `localfix.db`: The SQLite database where the generated relational data is housed.
3.  **Power BI Model:** A star-schema data model linking the tables, utilizing custom DAX formulas to calculate dynamic KPIs.

---
**Author:** Virat Solanki
