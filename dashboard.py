import streamlit as st

st.set_page_config(page_title="PhonePe Home", layout="wide")

st.title("🏠 Welcome to PhonePe Transaction Insights Dashboard")
st.markdown("""
This dashboard provides visual insights into **PhonePe Pulse** transaction data, including:

- 📈 Yearly and state-wise transaction performance
- 🔎 Filtered data by year, state, and type
- 📊 Interactive visualizations
- 💡 Business insights

Navigate using the sidebar to explore more.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/f/f8/PhonePe_Logo.png", width=300)
