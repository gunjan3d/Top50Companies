# 📊 Top 50 Indian Companies Dashboard

This project involves end-to-end **data extraction, transformation, and visualization** of the top 50 Indian companies by revenue, using the following tech stack:

- 🧠 **Python** (BeautifulSoup & Pandas)
- ☁️ **AWS EC2** for remote execution
- 📈 **Power BI** for interactive data visualization

---

## 📌 Project Objective

To scrape financial data about the top 50 Indian companies from Wikipedia, clean and process it for insights, and visualize it using Power BI to understand trends in revenue, profit, and sector-wise distribution.

---

## 🧱 Tech Stack

| Layer            | Tools Used            |
|------------------|------------------------|
| Data Extraction  | `BeautifulSoup`, `requests` |
| Data Processing  | `pandas`               |
| Hosting/Storage  | `AWS EC2`, `CSV`       |
| Visualization    | `Power BI`             |

---

## 🛠️ Workflow

### 1. 🔍 Web Scraping

- Source: [Wikipedia – List of largest Indian companies by revenue](https://en.wikipedia.org/wiki/List_of_largest_Indian_companies_by_revenue)
- Extracted:
  - Company name
  - Industry
  - Revenue (in ₹ crore)
  - Profit
  - Employees

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
```
2. 🧹 Data Cleaning & Transformation
Removed special characters and commas

Converted financial fields to numeric types

Renamed columns for readability

Saved cleaned dataset as top_50_indian_companies.csv

python
Copy
Edit
df['Revenue (₹ Cr)'] = df['Revenue (₹ Cr)'].str.replace(',', '').astype(float)
3. ☁️ Hosted Script on AWS EC2
Spun up a Ubuntu EC2 instance

Installed necessary Python packages

Ran and stored the output CSV file on the EC2 machine

Transferred CSV to local machine for visualization

📊 Visualization in Power BI
Key dashboards created:

Revenue by Industry: Bar chart comparison across sectors

Top 10 Companies by Profit: Horizontal bar graph

Employee Count vs Revenue: Bubble chart to compare company scale

Quarter-wise Revenue Trend (if extended)

Power BI features used:

Slicers for filtering by industry

Conditional formatting for high-revenue companies

Data cards for KPIs: total revenue, average profit, etc.

📁 Files
bash
Copy
Edit
top-50-indian-companies/
│
├── scrape_wikipedia.py       # Web scraping script
├── cleaned_data.csv          # Output dataset
├── powerbi_dashboard.pbix    # Power BI file
└── README.md
📈 Sample Output (Data Preview)
Company	Industry	Revenue (₹ Cr)	Profit (₹ Cr)	Employees
Reliance	Conglomerate	500000	39000	195000
TCS	IT Services	200000	38000	500000

👨‍💻 Author
Gunjan Sarode
