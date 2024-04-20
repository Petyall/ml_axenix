# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('data_hakaton1.csv')

# # Convert date columns to datetime format
# df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# # Extract year and month from Sale_Date
# df['Year'] = df['Sale_Date'].dt.year
# df['Month'] = df['Sale_Date'].dt.month

# # Group by Year, Month, and Product_Name and sum Quantity_Sold
# monthly_sales = df.groupby(['Year', 'Month', 'Product_Name'])['Quantity_Sold'].sum().reset_index()

# # Write the results to a new CSV file
# monthly_sales.to_csv('monthly_sales_statistics.csv', index=False)


import pandas as pd

# Read the CSV file
df = pd.read_csv('data_copy.csv')

# Convert date columns to datetime format
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# Extract year and month from Sale_Date
df['Year'] = df['Sale_Date'].dt.year
df['Month'] = df['Sale_Date'].dt.month

# Group by Year, Month, and Product_Name and sum Quantity_Sold
monthly_sales = df.groupby(['Year', 'Month', 'Product_Name'])['Quantity_Sold'].sum().reset_index()

# Calculate total sales per month per year
yearly_totals = monthly_sales.groupby(['Year', 'Month'])['Quantity_Sold'].sum().reset_index()

# Sort by sales to identify top and bottom months
yearly_totals['Rank'] = yearly_totals.groupby('Year')['Quantity_Sold'].rank(ascending=False, method='dense')

# Mark top 6 months with 1, bottom 6 months with 0
yearly_totals['Success'] = yearly_totals['Rank'].apply(lambda x: 1 if x <= 6 else 0)

# Merge with monthly_sales to add the Success column
monthly_sales = monthly_sales.merge(yearly_totals[['Year', 'Month', 'Success']], on=['Year', 'Month'], how='left')

# Fill NaN values with 0 in the Success column
monthly_sales['Success'] = monthly_sales['Success'].fillna(0)

# Write the results to a new CSV file
monthly_sales.to_csv('data_copy.csv', index=False)

