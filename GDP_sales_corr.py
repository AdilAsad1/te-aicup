import pandas as pd

# Read in the CSV file
df = pd.read_csv('bu1_erospace_Defense.csv')

# Calculate the correlation between sales_quantity and GDP_value
corr_qty_gdp = df['sales_quantity'].corr(df['GDP_value'])
print(f"Correlation between sales_quantity and GDP_value: {corr_qty_gdp}")

# Calculate the correlation between sales_amount and GDP_value
corr_amt_gdp = df['sales_amount'].corr(df['GDP_value'])
print(f"Correlation between sales_amount and GDP_value: {corr_amt_gdp}")