import pandas as pd


df = pd.read_csv('data_copy.csv')

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

df['Year'] = df['Sale_Date'].dt.year
df['Month'] = df['Sale_Date'].dt.month

monthly_sales = df.groupby(['Year', 'Month', 'Product_Name'])['Quantity_Sold'].sum().reset_index()

yearly_totals = monthly_sales.groupby(['Year', 'Month'])['Quantity_Sold'].sum().reset_index()

yearly_totals['Rank'] = yearly_totals.groupby('Year')['Quantity_Sold'].rank(ascending=False, method='dense')

yearly_totals['Success'] = yearly_totals['Rank'].apply(lambda x: 1 if x <= 6 else 0)

monthly_sales = monthly_sales.merge(yearly_totals[['Year', 'Month', 'Success']], on=['Year', 'Month'], how='left')

monthly_sales['Success'] = monthly_sales['Success'].fillna(0)

monthly_sales.to_csv('data_copy.csv', index=False)

