import pandas as pd


sales_data = pd.read_csv('data_hakaton1.csv')

sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

def calculate_coefficients(data, product_name):
    filtered_data = data[data['Product_Name'] == product_name]
    years = filtered_data['Sale_Date'].dt.year.unique()

    coefficients_data = []
    average_prices = []

    for year in years:
        year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
        total_demand_year = year_data['Quantity_Sold'].sum()
        average_demand_year = total_demand_year / 12
        
        for month in range(1, 13):
            month_data = year_data[year_data['Sale_Date'].dt.month == month]
            demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
            
            average_price = month_data['Product_Cost'].mean()
            average_price = average_price
            average_prices.append(average_price)
            
            average_average_price = sum(average_prices) / len(average_prices)
            
            condition = (demand_coefficient > average_demand_year) & (average_price < average_average_price)
            new_column_value = 1 if condition else 0
            
            coefficients_data.append({
                'Product_Name': product_name,
                'Year': year,
                'Month': month,
                'Demand_Coefficient': demand_coefficient,
                'Average_Price': average_price,
                'New_Column_Name': new_column_value,
            })

    return pd.DataFrame(coefficients_data)

all_coefficients_df = pd.DataFrame()
unique_products = sales_data['Product_Name'].unique()
for product_name in unique_products:
    coefficients_df = calculate_coefficients(sales_data, product_name)
    all_coefficients_df = pd.concat([all_coefficients_df, coefficients_df])

all_coefficients_df.to_csv('data_hakaton1_with_coefficients.csv', index=False)

sales_data = pd.read_csv('data_hakaton1.csv')
coefficients_data = pd.read_csv('data_hakaton1_with_coefficients.csv')

sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])
coefficients_data['Year'] = coefficients_data['Year'].astype(str)
coefficients_data['Month'] = coefficients_data['Month'].astype(str)

merged_data = pd.merge(sales_data, coefficients_data, 
                       left_on=['Product_Name', sales_data['Sale_Date'].dt.year.astype(str), sales_data['Sale_Date'].dt.month.astype(str)],
                       right_on=['Product_Name', 'Year', 'Month'],
                       how='left')

merged_data.to_csv('merged_data_hakaton.csv', index=False)
