import pandas as pd


df = pd.read_csv('merged_data_hakaton.csv')

df['Manufacture_Date'] = pd.to_datetime(df['Manufacture_Date'])
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

df['Days_for_sale'] = (df['Expiry_Date'] - df['Manufacture_Date']).dt.days

df['Comparison'] = df['Days_for_sale'] - (df['Sale_Date'] - df['Manufacture_Date']).dt.days
df['Sales_Velocity_Coefficient'] = df.apply(lambda row: 1 if row['Comparison'] < row['Days_for_sale']/2 else 0, axis=1)

df.to_csv('all_data.csv', index=False)
