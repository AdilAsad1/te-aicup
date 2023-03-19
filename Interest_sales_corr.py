import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv('bu5_channel_data_devices.csv')

# Calculate the correlation between sales_quantity and Interest_Rate
corr1 = df['sales_quantity'].corr(df['Interest_rate'])

# Calculate the correlation between sales_amount and Interest_Rate
corr2 = df['sales_amount'].corr(df['Interest_rate'])

# Print the results
print('Correlation between sales_quantity and Interest_Rate:', corr1)
print('Correlation between sales_amount and Interest_Rate:', corr2)
