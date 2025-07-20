import mysql.connector
import pandas as pd

# ✅ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",  # Change this to your MySQL root password
)
cursor = conn.cursor()

# ✅ Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_db")
cursor.execute("USE phonepe_db")

# ✅ Drop table if already exists
cursor.execute("DROP TABLE IF EXISTS aggregated_transaction")

# ✅ Create table
create_table_query = """
CREATE TABLE aggregated_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    count BIGINT,
    amount DOUBLE
)
"""
cursor.execute(create_table_query)
print("✅ Table created successfully!")

# ✅ Load CSV
df = pd.read_csv("aggregated_transaction_data.csv")

# ✅ Insert data into table
insert_query = """
INSERT INTO aggregated_transaction (state, year, quarter, transaction_type, count, amount)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_query, df.to_records(index=False).tolist())



conn.commit()
print(f"✅ Inserted {cursor.rowcount} rows into the table.")

# ✅ Close connection
cursor.close()
conn.close()
print("✅ MySQL connection closed.")
    