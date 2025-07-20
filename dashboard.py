import streamlit as st
import base64

# ✅ Page setup
st.set_page_config(page_title="PhonePe Home", layout="wide")

# ✅ Function to set a local image as background
def set_bg_image_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .main > div {{
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    h1, h2, h3 {{
        color: #003366;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ✅ Apply background
# ✅ Apply background (correct file name now)
set_bg_image_local("chart_preview.webp")


# ✅ Main content
st.title("📊 Welcome to PhonePe Pulse Dashboard")

st.markdown("""
This interactive dashboard is built using **Python, MySQL, and Streamlit**.  
It lets you explore India's digital payment insights from the PhonePe Pulse data.

---

### 🧭 Sidebar Navigation

Use the **left-hand sidebar** to explore:

- 📈 **Charts** – Transaction trends by year, state, and type  
- 📊 **Raw Data** – Table + Download CSV  
- 💡 **Insights** – Business patterns and recommendations  

---

### 📌 Important:
Ensure your MySQL server is running and database `phonepe_db` is active before viewing charts or data.

---

Explore the dashboard and gain data-driven insights from PhonePe transactions across India!
""")
