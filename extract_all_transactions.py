import os
import json
import pandas as pd

base_path = "pulse/data/aggregated/transaction/country/india/state/"
all_states = os.listdir(base_path)

all_data = []

for state in all_states:
    state_path = os.path.join(base_path, state)
    if os.path.isdir(state_path):
        years = os.listdir(state_path)
        for year in years:
            year_path = os.path.join(state_path, year)
            quarters = os.listdir(year_path)
            for quarter_file in quarters:
                quarter_path = os.path.join(year_path, quarter_file)
                with open(quarter_path, 'r') as f:
                    try:
                        data = json.load(f)
                        quarter_num = int(quarter_file.split('.')[0])
                        for item in data['data']['transactionData']:
                            transaction_type = item['name']
                            count = item['paymentInstruments'][0]['count']
                            amount = item['paymentInstruments'][0]['amount']
                            all_data.append({
                                'state': state.replace('-', ' ').title(),
                                'year': int(year),
                                'quarter': quarter_num,
                                'transaction_type': transaction_type,
                                'count': count,
                                'amount': amount
                            })
                    except Exception as e:
                        print(f"Error processing {quarter_path}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Preview top 10 rows
print(df.head(10))

# Save to CSV (optional)
df.to_csv("aggregated_transaction_data.csv", index=False)
