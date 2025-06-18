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
