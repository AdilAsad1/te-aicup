import pandas as pd

# Read in the first CSV file
df1 = pd.read_csv('bu5_channel_data_devices.csv')

# Read in the second CSV file
df2 = pd.read_excel('ConsumerSentiment.xlsx')

# Merge the two dataframes based on matching fiscal year and month
df_merged = pd.merge(df1, df2, how='left', left_on=['fiscal_year_historical', 'fiscal_month_historical'], right_on=['Year', 'Month'])

# Rename the UMCSENT column to 'CSENT' and drop the original 'Year' and 'Month' columns
df_merged = df_merged.rename(columns={'UMCSENT': 'CSENT'}).drop(columns=['Year', 'Month'])

# Save the merged dataframe to a new CSV file
df_merged.to_csv('bu5_channel_data_devices.csv', index=False)