import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",  # Replace with your MySQL password
    database="phonepe_db"
)
cursor = conn.cursor()

def run_query(query, columns):
    cursor.execute(query)
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=columns)

# 1️⃣ Total Transaction Amount Per Year
df_year = run_query("""
    SELECT year, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY year
    ORDER BY year;
""", ["Year", "Total_Amount"])
print("\n📊 Total Transaction Amount Per Year:\n", df_year)

# 📊 Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df_year["Year"], df_year["Total_Amount"], color='skyblue')
plt.title("Total Transaction Amount Per Year")
plt.xlabel("Year")
plt.ylabel("Total Amount (in ₹)")
plt.xticks(df_year["Year"])
plt.tight_layout()
plt.show()

# 2️⃣ Top 5 States by Total Transaction Amount
df_states = run_query("""
    SELECT state, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY state
    ORDER BY total_amount DESC
    LIMIT 5;
""", ["State", "Total_Amount"])
print("\n📊 Top 5 States by Total Transaction Amount:\n", df_states)

# 📊 Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(df_states["Total_Amount"], labels=df_states["State"], autopct="%1.1f%%", startangle=140)
plt.title("Top 5 States by Total Transaction Amount")
plt.tight_layout()
plt.show()

# 3️⃣ Most Popular Transaction Types Overall
df_types = run_query("""
    SELECT transaction_type, SUM(count) AS total_count
    FROM aggregated_transaction
    GROUP BY transaction_type
    ORDER BY total_count DESC;
""", ["Transaction_Type", "Total_Count"])
print("\n📊 Most Popular Transaction Types:\n", df_types)

# 📊 Horizontal Bar Chart
plt.figure(figsize=(8, 5))
plt.barh(df_types["Transaction_Type"], df_types["Total_Count"], color='lightgreen')
plt.title("Most Popular Transaction Types")
plt.xlabel("Total Count")
plt.ylabel("Transaction Type")
plt.tight_layout()
plt.show()

# 4️⃣ Total Transactions Per Quarter
df_quarter = run_query("""
    SELECT quarter, SUM(count) AS total_transactions
    FROM aggregated_transaction
    GROUP BY quarter
    ORDER BY quarter;
""", ["Quarter", "Total_Transactions"])
print("\n📊 Total Transactions Per Quarter:\n", df_quarter)

# 📊 Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df_quarter["Quarter"], df_quarter["Total_Transactions"], color='orange')
plt.title("Total Transactions Per Quarter")
plt.xlabel("Quarter")
plt.ylabel("Total Transactions")
plt.xticks(df_quarter["Quarter"])
plt.tight_layout()
plt.show()

# 5️⃣ State with Highest Peer-to-Peer Payments
df_peer = run_query("""
    SELECT state, SUM(count) AS peer_to_peer_count
    FROM aggregated_transaction
    WHERE transaction_type = 'Peer-to-peer payments'
    GROUP BY state
    ORDER BY peer_to_peer_count DESC
    LIMIT 1;
""", ["State", "Peer_To_Peer_Count"])
print("\n📊 State with Highest Peer-to-Peer Payments:\n", df_peer)

# ✅ Close connection
cursor.close()
conn.close()
