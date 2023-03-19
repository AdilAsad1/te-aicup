import pandas as pd

# Read in the CSV file
df1 = pd.read_csv('bu1_erospace_Defense.csv')

# Read in the Excel file
df2 = pd.read_excel('GDP1.xlsx')

# Merge the two dataframes based on matching fiscal year and quarter
df_merged = pd.merge(df1, df2, how='left', left_on=['fiscal_year_historical', 'fiscal_quarter_historical'], right_on=['Year', 'Quarter'])

# Rename the GDP column to 'GDP' and drop the original 'Year' and 'Quarter' columns
df_merged = df_merged.rename(columns={'GDP': 'GDP_value'}).drop(columns=['Year', 'Quarter'])

# Save the merged dataframe to a new CSV file
df_merged.to_csv('bu1_erospace_Defense.csv', index=False)
