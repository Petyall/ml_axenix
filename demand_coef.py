import pandas as pd

# Чтение данных из CSV файла
sales_data = pd.read_csv('data_hakaton1.csv')

# Преобразование столбца Sale_Date в формат datetime
sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# Функция для расчета коэффициента спроса и цены за месяц
def calculate_coefficients(data, product_name):
    # Фильтруем данные по имени продукта и году
    filtered_data = data[data['Product_Name'] == product_name]
    years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
    # Список для хранения данных коэффициентов
    coefficients_data = []
    
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
            
            coefficients_data.append({
                'Product_Name': product_name,
                'Year': year,
                'Month': month,
                'Demand_Coefficient': demand_coefficient,
            })
    
    return coefficients_data

# Пример использования функции для расчета коэффициентов для продукта "Огурец"
coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# Преобразование данных в DataFrame
coefficients_df = pd.DataFrame(coefficients_data)

# Сохранение данных в CSV файл
coefficients_df.to_csv('coefficients_data.csv', index=False)