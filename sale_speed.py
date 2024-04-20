# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('data_hakaton1.csv')

# # Convert date columns to datetime format
# df['Manufacture_Date'] = pd.to_datetime(df['Manufacture_Date'])
# df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])
# df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# # Calculate the number of days for sale
# df['Days_for_sale'] = (df['Expiry_Date'] - df['Manufacture_Date']).dt.days

# # Calculate the comparison number and sales velocity coefficient
# df['Comparison'] = df['Days_for_sale'] - (df['Sale_Date'] - df['Manufacture_Date']).dt.days
# df['Sales_Velocity_Coefficient'] = df.apply(lambda row: 1 if row['Comparison'] < row['Days_for_sale']/2 else 0, axis=1)

# # Write the results to a new CSV file
# df.to_csv('sales_velocity_results.csv', index=False)



import pandas as pd

# Read the CSV file
df = pd.read_csv('merged_data_hakaton.csv')

# Convert date columns to datetime format
df['Manufacture_Date'] = pd.to_datetime(df['Manufacture_Date'])
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# Calculate the number of days for sale
df['Days_for_sale'] = (df['Expiry_Date'] - df['Manufacture_Date']).dt.days

# Calculate the comparison number and sales velocity coefficient
df['Comparison'] = df['Days_for_sale'] - (df['Sale_Date'] - df['Manufacture_Date']).dt.days
df['Sales_Velocity_Coefficient'] = df.apply(lambda row: 1 if row['Comparison'] < row['Days_for_sale']/2 else 0, axis=1)

# Write the results back to the same CSV file
df.to_csv('all_data.csv', index=False)
