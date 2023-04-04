import pandas as pd

# Read in the CSV file
df = pd.read_csv('fulldata1.csv')

# Calculate the correlation between sales_quantity and GDP_value
corr_qty_fuel = df['sales_quantity'].corr(df['FuelPrice'])
print(f"Correlation between sales_quantity and Fuel Price: {corr_qty_fuel}")

# Calculate the correlation between sales_amount and GDP_value
corr_amt_fuel = df['sales_amount'].corr(df['GDP_value'])
print(f"Correlation between sales_amount and Fuel Price: {corr_amt_fuel}")