import pandas as pd

# Load the first CSV file into a pandas dataframe
df1 = pd.read_csv('bu5_channel_data_devices.csv')

# Load the second CSV file into a pandas dataframe
df2 = pd.read_excel('Inflation.xlsx')

# Merge the two dataframes on the Year and Month columns
merged_df = pd.merge(df1, df2, left_on=['fiscal_year_historical', 'fiscal_month_historical'],
                     right_on=['year', 'month'], how='left')

# Rename the CORESTICKM159SFRBATL column to Inflation
merged_df.rename(columns={'CORESTICKM159SFRBATL': 'Inflation'}, inplace=True)

# Drop the year and month columns from the merged dataframe
merged_df.drop(['year', 'month', 'observation_date'], axis=1, inplace=True)

# Save the modified dataframe as a new CSV file
merged_df.to_csv('bu5_channel_data_devices.csv', index=False)