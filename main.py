# import csv

# def get_unique_values_from_csv_column(file_path, column_name, encoding='utf-8'):
#     unique_values = set()
#     with open(file_path, newline='', encoding=encoding) as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if column_name in row:
#                 unique_values.add(row[column_name])
#     return list(unique_values)

# # Пример использования:
# file_path = 'data_hakaton1.csv'
# column_name = 'Product_Name'
# unique_values = get_unique_values_from_csv_column(file_path, column_name)
# print(unique_values)



# ['Мед', 'Курица', 'Хлеб', 'Яблоки', 'Кефир', 'Молоко', 'Рис', 'Морковь', 'Творог', 'Капуста', 'Масло', 'Картофель', 'Куриное яйцо', 'Сливочное масло', 'Свинина', 'Свекла', 'Оливковое масло', 'Огурцы маринованные', 'Огурцы', 'Сыр']


# import pandas as pd

# # Загрузка CSV файла
# df = pd.read_csv('data_hakaton1.csv')

# # Преобразование даты продажи в формат datetime
# df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# # Расчет суммы продаж за месяц и за год для каждого уникального товара и месяца
# grouped = df.groupby(['Product_Name', df['Sale_Date'].dt.month])

# # Расчет суммы продаж за месяц и за год
# monthly_sales = grouped['Quantity_Sold'].sum()
# yearly_sales = grouped['Quantity_Sold'].sum().groupby('Product_Name').mean()

# # Расчет коэффициента спроса
# demand_coefficient = monthly_sales / yearly_sales

# # Расчет средней выручки за год и за месяц
# yearly_revenue = grouped['Product_Amount'].sum().groupby('Product_Name').mean()
# monthly_revenue = grouped['Product_Amount'].sum()

# # Расчет коэффициента цены
# price_coefficient = monthly_revenue / yearly_revenue

# # Формирование DataFrame с результатами
# results = pd.DataFrame({
#     'Demand_Coefficient': demand_coefficient,
#     'Price_Coefficient': price_coefficient
# })

# # Присвоение значения 1 или 0 в поле сезонности
# results['Seasonality'] = results.apply(lambda row: 1 if row['Demand_Coefficient'] > 1 and row['Price_Coefficient'] < 1 else 0, axis=1)

# # Сохранение результатов в новый CSV файл
# results.to_csv('результаты.csv', index=True)




# import pandas as pd

# # Чтение данных из CSV файла
# sales_data = pd.read_csv('data_hakaton1.csv')

# # Преобразование столбца Sale_Date в формат datetime
# sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# # Функция для расчета коэффициента спроса и цены за месяц
# def calculate_coefficients(data, product_name):
#     # Фильтруем данные по имени продукта и году
#     filtered_data = data[data['Product_Name'] == product_name]
#     years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
#     # Список для хранения данных коэффициентов
#     coefficients_data = []
    
#     # Расчет коэффициентов для каждого года
#     for year in years:
#         year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
#         # Расчет среднего спроса за год
#         total_demand_year = year_data['Quantity_Sold'].sum()
#         average_demand_year = total_demand_year / 12
        
#         # Расчет средней стоимости товаров за год
#         year_data['Total_Cost'] = year_data['Quantity_Sold'] * year_data['Product_Cost']
#         average_cost_year = year_data.groupby(year_data['Sale_Date'].dt.month)['Total_Cost'].mean()
        
#         # Расчет коэффициента спроса и цены за месяц
#         for month, average_cost in average_cost_year.items():
#             month_data = year_data[year_data['Sale_Date'].dt.month == month]
#             demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
#             price_coefficient = month_data['Total_Cost'].sum() / average_cost
            
#             coefficients_data.append({
#                 'Product_Name': product_name,
#                 'Year': year,
#                 'Month': month,
#                 'Demand_Coefficient': demand_coefficient,
#                 'Price_Coefficient': price_coefficient
#             })
    
#     return coefficients_data

# # Пример использования функции для расчета коэффициентов для продукта "Огурец"
# coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# # Преобразование данных в DataFrame
# coefficients_df = pd.DataFrame(coefficients_data)

# # Сохранение данных в CSV файл
# coefficients_df.to_csv('coefficients_data.csv', index=False)


# import pandas as pd

# # Чтение данных из CSV файла
# sales_data = pd.read_csv('data_hakaton1.csv')

# # Функция для расчета коэффициентов спроса и цены
# def calculate_coefficients(data, product_name):
#     # Фильтрация данных по имени продукта
#     filtered_data = data[data['Product_Name'] == product_name]
    
#     # Группировка данных по году и месяцу
#     grouped_data = filtered_data.groupby([filtered_data['Sale_Date'].dt.year, filtered_data['Sale_Date'].dt.month])
    
#     # Список для хранения результатов
#     results = []
    
#     # Расчет коэффициентов для каждого года и месяца
#     for (year, month), group in grouped_data:
#         total_demand_year = group['Quantity_Sold'].sum()  # Сумма проданных товаров за год
#         average_demand_year = total_demand_year / 12  # Средний спрос за год
        
#         # Расчет коэффициента спроса
#         demand_coefficient = group['Quantity_Sold'].sum() / average_demand_year
        
#         # Расчет средней цены товара
#         average_price = group['Product_Cost'].mean()
        
#         results.append({
#             'Year': year,
#             'Month': month,
#             'Demand_Coefficient': demand_coefficient,
#             'Average_Price': average_price
#         })
    
#     return results

# # Преобразование столбца Sale_Date в тип данных datetime
# sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# # Вызов функции calculate_coefficients
# coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# # Преобразование данных в DataFrame
# coefficients_df = pd.DataFrame(coefficients_data)

# # Сохранение данных в новый CSV файл
# coefficients_df.to_csv('coefficients_data.csv', index=False)




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

# Пример использования функции для расчета коэффициентов для продукта "Огурец"
coefficients_df, coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# Сохранение данных в CSV файл
coefficients_df.to_csv('coefficients_data.csv', index=False)
