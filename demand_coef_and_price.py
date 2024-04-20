import pandas as pd

sales_data = pd.read_csv('data_hakaton1.csv')

# Преобразование столбца Sale_Date в формат datetime
sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# Функция для расчета коэффициента спроса и цены за месяц
def calculate_coefficients(data, product_name):
    # Фильтруем данные по имени продукта и году
    filtered_data = data[data['Product_Name'] == product_name]
    years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
    # Список для хранения данных коэффициентов и средних цен
    coefficients_data = []
    average_prices = []  # Для хранения средних цен за месяц
    
    # Расчет коэффициентов для каждого года
    for year in years:
        year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
        # Расчет среднего спроса за год
        total_demand_year = year_data['Quantity_Sold'].sum()
        average_demand_year = total_demand_year / 12
        
        # Расчет коэффициента спроса и цены за месяц
        for month in range(1, 13):
            month_data = year_data[year_data['Sale_Date'].dt.month == month]
            demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
            
            # Расчет средней цены за месяц
            average_price = month_data['Product_Cost'].mean()
            average_prices.append(average_price)
            
            coefficients_data.append({
                'Product_Name': product_name,
                'Year': year,
                'Month': month,
                'Demand_Coefficient': demand_coefficient,
            })
    
    # Преобразование данных в DataFrame
    coefficients_df = pd.DataFrame(coefficients_data)
    # Добавление средних цен в DataFrame
    coefficients_df['Average_Price'] = average_prices
    
    return coefficients_df, coefficients_data

coefficients_df, coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# Сохранение данных в CSV файл
coefficients_df.to_csv('coefficients_data.csv', index=False)