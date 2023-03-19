import pandas as pd

# Load the first CSV file into a pandas dataframe
df1 = pd.read_csv('bu5_channel_data_devices.csv')

# Load the second CSV file into a pandas dataframe
df2 = pd.read_excel('InterestRate.xlsx')

# Merge the two dataframes on the Year and Month columns
merged_df = pd.merge(df1, df2, left_on=['fiscal_year_historical', 'fiscal_month_historical'],
                     right_on=['Year', 'Month'], how='left')

# Rename the INTDSRUSM193N column to Interest_rate
merged_df.rename(columns={'INTDSRUSM193N': 'Interest_rate'}, inplace=True)

# Drop the Year and Month columns from the merged dataframe
merged_df.drop(['Year', 'Month','DATE_y' ], axis=1, inplace=True)

# Save the modified dataframe as a new CSV file
merged_df.to_csv('bu5_channel_data_devices.csv', index=False)