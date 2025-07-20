import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# 🔌 Connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # 🔁 Your MySQL username
        password="12345",  # 🔁 Your MySQL password
        database="phonepe_db"
    )

# 🔽 Dropdown filter values
@st.cache_data
def get_filter_options():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT year FROM aggregated_transaction ORDER BY year")
    years = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT state FROM aggregated_transaction ORDER BY state")
    states = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT transaction_type FROM aggregated_transaction ORDER BY transaction_type")
    types = [row[0] for row in cursor.fetchall()]

    conn.close()
    return years, states, types

# 📥 Filtered transaction data
@st.cache_data
def get_filtered_data(year, state, t_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT year, state, transaction_type, count, amount
        FROM aggregated_transaction
        WHERE year = %s AND state = %s AND transaction_type = %s
    """, (year, state, t_type))
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result, columns=["Year", "State", "Transaction_Type", "Count", "Amount"])

# 📥 Yearly totals
@st.cache_data
def fetch_yearly_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT year, SUM(amount) AS total_amount
        FROM aggregated_transaction
        GROUP BY year
        ORDER BY year;
    """)
    results = cursor.fetchall()
    conn.close()
    return pd.DataFrame(results, columns=["Year", "Total_Amount"])

# 📥 Top 5 states
@st.cache_data
def fetch_top_states():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT state, SUM(amount) AS total_amount
        FROM aggregated_transaction
        GROUP BY state
        ORDER BY total_amount DESC
        LIMIT 5;
    """)
    results = cursor.fetchall()
    conn.close()
    return pd.DataFrame(results, columns=["State", "Total_Amount"])

# 📥 Transaction types
@st.cache_data
def fetch_transaction_types():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT transaction_type, SUM(count) AS total_count
        FROM aggregated_transaction
        GROUP BY transaction_type
        ORDER BY total_count DESC;
    """)
    results = cursor.fetchall()
    conn.close()
    return pd.DataFrame(results, columns=["Transaction_Type", "Total_Count"])

# 🖥️ Streamlit App
st.set_page_config(page_title="PhonePe Dashboard", layout="wide")
st.title("📊 PhonePe Transaction Insights Dashboard")

# 🔎 Sidebar Filters
st.sidebar.header("🔎 Filter Data")
years, states, types = get_filter_options()

selected_year = st.sidebar.selectbox("Select Year", years)
selected_state = st.sidebar.selectbox("Select State", states)
selected_type = st.sidebar.selectbox("Select Transaction Type", types)

# 📋 Filtered Results
st.subheader("📋 Filtered Transaction Data")
filtered_df = get_filtered_data(selected_year, selected_state, selected_type)
st.dataframe(filtered_df)

# 📊 Yearly Chart
st.subheader("📈 Total Transaction Amount Per Year")
df_year = fetch_yearly_data()
st.bar_chart(df_year.set_index("Year"))

# 🥧 Top 5 States Chart
st.subheader("🏆 Top 5 States by Transaction Amount")
df_states = fetch_top_states()
fig1, ax1 = plt.subplots()
ax1.pie(df_states["Total_Amount"], labels=df_states["State"], autopct="%1.1f%%", startangle=140)
ax1.axis("equal")
st.pyplot(fig1)

# 📈 Transaction Types Chart
st.subheader("📌 Most Popular Transaction Types")
df_types = fetch_transaction_types()
st.bar_chart(df_types.set_index("Transaction_Type"))
