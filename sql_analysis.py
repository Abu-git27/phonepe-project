import mysql.connector
import pandas as pd

# ✅ Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",   # Change to your MySQL password
    database="phonepe_db"
)
cursor = conn.cursor()

# 🧠 Query 1: Total Transaction Amount Per Year
query = """
SELECT year, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;
"""

cursor.execute(query)

# 🔄 Fetch into Pandas DataFrame
results = cursor.fetchall()
columns = [i[0] for i in cursor.description]
df = pd.DataFrame(results, columns=columns)

# 🖨 Print Results
print("\n📊 Total Transaction Amount Per Year:\n")
print(df)

# ✅ Close connection
cursor.close()
conn.close()
