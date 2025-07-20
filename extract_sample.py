import json
import pandas as pd

# Update the path to match your structure if needed
file_path = "pulse/data/aggregated/transaction/country/india/state/andaman-&-nicobar-islands/2018/1.json"

# Load JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to extract transaction data
def extract_transaction_data(data, state, year, quarter):
    transactions = []
    for item in data['data']['transactionData']:
        transaction_type = item['name']
        count = item['paymentInstruments'][0]['count']
        amount = item['paymentInstruments'][0]['amount']
        transactions.append({
            'state': state,
            'year': year,
            'quarter': quarter,
            'transaction_type': transaction_type,
            'count': count,
            'amount': amount
        })
    return transactions

# Create DataFrame
df = pd.DataFrame(extract_transaction_data(data, "Andaman & Nicobar Islands", 2018, 1))

# Print result
print(df)
