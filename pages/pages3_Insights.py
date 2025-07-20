import streamlit as st

st.set_page_config(page_title="Insights", layout="wide")
st.title("💡 Business Insights")

st.markdown("""
### 📌 Key Observations:

- 🏆 **Karnataka, Maharashtra, and Tamil Nadu** lead in transaction volumes.
- 📈 **2019–2021** show rapid UPI growth year-over-year.
- 🤝 **Peer-to-peer** is the most popular transaction type overall.
- 💡 **Financial Services** category, though low in volume, shows consistent growth.

---

### 🎯 Recommendations:

- 📍 Focus marketing in top-performing southern states.
- 📊 Expand services in under-performing regions using district-level analysis.
- 🔐 Apply fraud detection in high-amount segments.

---

_Note: More insights will be derived from full data once map/user/insurance categories are analyzed._
""")
