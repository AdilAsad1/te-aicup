import pandas as pd

# Read in the CSV file
df = pd.read_csv('bu5_channel_data_devices.csv')

# Calculate the correlation between sales_quantity and CSENT
corr_qty_csent = df['sales_quantity'].corr(df['CSENT'])
print(f"Correlation between sales_quantity and CSENT: {corr_qty_csent}")

# Calculate the correlation between sales_amount and CSENT
corr_amt_csent = df['sales_amount'].corr(df['CSENT'])
print(f"Correlation between sales_amount and CSENT: {corr_amt_csent}")
