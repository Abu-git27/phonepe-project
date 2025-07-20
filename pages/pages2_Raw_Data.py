import streamlit as st
import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Change as needed
        database="phonepe_db"
    )

@st.cache_data
def get_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM aggregated_transaction LIMIT 100")
    data = cur.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=["ID", "State", "Year", "Quarter", "Type", "Count", "Amount"])

st.set_page_config(page_title="Raw Data", layout="wide")
st.title("📊 Raw Transaction Data")

df = get_data()
st.dataframe(df, use_container_width=True)

st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False),
    file_name="phonepe_data_sample.csv",
    mime="text/csv"
)
