# 📊 PhonePe Transaction Insights – Data Science Project

This project analyzes and visualizes digital transaction data from the [PhonePe Pulse](https://github.com/PhonePe/pulse) repository. It includes data extraction from JSON files, SQL integration, exploratory data analysis, and interactive dashboards built with Streamlit.

---

## 🚀 Project Goals

- Extract and structure raw PhonePe transaction data
- Store data in a relational database (MySQL)
- Perform EDA and visualize patterns in user behavior and transaction categories
- Build a Streamlit dashboard for real-time data exploration
- Generate insights to support business decisions

---

## 📁 Project Structure

phonepe_project/
├── pulse/ # Cloned PhonePe Pulse dataset
├── extract_sample.py # Sample extractor for single JSON
├── extract_all_transactions.py # Full transaction data extractor
├── aggregated_transaction_data.csv # Cleaned full dataset
├── README.md # Project documentation
├── venv/ # Virtual environment (ignored)
└── requirements.txt # Python dependencies (optional)