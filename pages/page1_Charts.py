import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Change as needed
        database="phonepe_db"
    )

st.set_page_config(page_title="Charts", layout="wide")
st.title("📈 Transaction Charts")

@st.cache_data
def fetch_year_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT year, SUM(amount) FROM aggregated_transaction GROUP BY year")
    data = cur.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=["Year", "Total_Amount"])

@st.cache_data
def fetch_top_states():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT state, SUM(amount) FROM aggregated_transaction GROUP BY state ORDER BY SUM(amount) DESC LIMIT 5")
    data = cur.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=["State", "Total_Amount"])

df_year = fetch_year_data()
df_states = fetch_top_states()

st.subheader("💰 Total Transaction Amount Per Year")
st.bar_chart(df_year.set_index("Year"))

st.subheader("🏆 Top 5 States by Transaction Amount")
fig, ax = plt.subplots()
ax.pie(df_states["Total_Amount"], labels=df_states["State"], autopct="%1.1f%%")
ax.axis("equal")
st.pyplot(fig)
