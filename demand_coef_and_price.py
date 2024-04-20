# import pandas as pd
# import random

# sales_data = pd.read_csv('data_hakaton1.csv')

# # Преобразование столбца Sale_Date в формат datetime
# sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# def multiply_with_random():
#     random_factor = random.uniform(0.1, 0.9)
#     return random_factor

# # Функция для расчета коэффициента спроса и цены за месяц
# def calculate_coefficients(data, product_name):
#     # Фильтруем данные по имени продукта и году
#     filtered_data = data[data['Product_Name'] == product_name]
#     years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
#     # Список для хранения данных коэффициентов и средних цен
#     coefficients_data = []
#     average_prices = []  # Для хранения средних цен за месяц

    
#     # Расчет коэффициентов для каждого года
#     for year in years:
#         year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
#         # Расчет среднего спроса за год
#         total_demand_year = year_data['Quantity_Sold'].sum()
#         average_demand_year = total_demand_year / 12
        
#         # Расчет коэффициента спроса и цены за месяц
#         for month in range(1, 13):
#             month_data = year_data[year_data['Sale_Date'].dt.month == month]
#             demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
            
#             # Расчет средней цены за месяц
#             average_price = month_data['Product_Cost'].mean()
#             average_price = average_price / multiply_with_random()
#             average_prices.append(average_price)
            
#             coefficients_data.append({
#                 'Product_Name': product_name,
#                 'Year': year,
#                 'Month': month,
#                 'Demand_Coefficient': demand_coefficient*multiply_with_random(),
#             })

    
#     # Преобразование данных в DataFrame
#     coefficients_df = pd.DataFrame(coefficients_data)
#     # Добавление средних цен в DataFrame
#     coefficients_df['Average_Price'] = average_prices
    
#     return coefficients_df, coefficients_data

# coefficients_df, coefficients_data = calculate_coefficients(sales_data, 'Огурцы')

# # Сохранение данных в CSV файл
# coefficients_df.to_csv('coefficients_data.csv', index=False)


# import pandas as pd
# import random

# sales_data = pd.read_csv('data_hakaton1.csv')

# # Преобразование столбца Sale_Date в формат datetime
# sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# def multiply_with_random():
#     random_factor = random.uniform(0.1, 0.9)
#     return random_factor

# # Функция для расчета коэффициента спроса и цены за месяц
# def calculate_coefficients(data, product_name):
#     # Фильтруем данные по имени продукта и году
#     filtered_data = data[data['Product_Name'] == product_name]
#     years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
#     # Список для хранения данных коэффициентов и средних цен
#     coefficients_data = []
#     average_prices = []  # Для хранения средних цен за месяц

#     # Расчет коэффициентов для каждого года
#     for year in years:
#         year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
#         # Расчет среднего спроса за год
#         total_demand_year = year_data['Quantity_Sold'].sum()
#         average_demand_year = total_demand_year / 12
        
#         # Расчет коэффициента спроса и цены за месяц
#         for month in range(1, 13):
#             month_data = year_data[year_data['Sale_Date'].dt.month == month]
#             demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
            
#             # Расчет средней цены за месяц
#             average_price = month_data['Product_Cost'].mean()
#             average_price = average_price / multiply_with_random()
#             average_prices.append(average_price)
            
#             coefficients_data.append({
#                 'Product_Name': product_name,
#                 'Year': year,
#                 'Month': month,
#                 'Demand_Coefficient': demand_coefficient * multiply_with_random(),
#                 'Average_Price': average_price,  # Добавляем среднюю цену в данные
#             })

#     return pd.DataFrame(coefficients_data)

# # Расчет коэффициентов для всех продуктов
# all_coefficients_df = pd.DataFrame()
# unique_products = sales_data['Product_Name'].unique()
# for product_name in unique_products:
#     coefficients_df = calculate_coefficients(sales_data, product_name)
#     all_coefficients_df = pd.concat([all_coefficients_df, coefficients_df])

# # Сохранение данных в CSV файл
# all_coefficients_df.to_csv('data_hakaton1_with_coefficients.csv', index=False)



import pandas as pd
import random

sales_data = pd.read_csv('data_hakaton1.csv')

# Преобразование столбца Sale_Date в формат datetime
sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

def multiply_with_random():
    random_factor = random.uniform(0.5, 0.9)
    return random_factor

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
            # average_price = average_price
            average_price = average_price / multiply_with_random()
            average_prices.append(average_price)
            
            # Расчет средней арифметической цены за год
            average_average_price = sum(average_prices) / len(average_prices)
            
            # Логика для нового столбца
            condition = (demand_coefficient > average_demand_year) & (average_price < average_average_price)
            new_column_value = 1 if condition else 0
            
            coefficients_data.append({
                'Product_Name': product_name,
                'Year': year,
                'Month': month,
                'Demand_Coefficient': demand_coefficient,
                # 'Demand_Coefficient': demand_coefficient * multiply_with_random(),
                'Average_Price': average_price,  # Добавляем среднюю цену в данные
                'New_Column_Name': new_column_value,  # Добавляем новый столбец с логикой
            })

    return pd.DataFrame(coefficients_data)

# Расчет коэффициентов для всех продуктов
all_coefficients_df = pd.DataFrame()
unique_products = sales_data['Product_Name'].unique()
for product_name in unique_products:
    coefficients_df = calculate_coefficients(sales_data, product_name)
    all_coefficients_df = pd.concat([all_coefficients_df, coefficients_df])

# Сохранение данных в CSV файл
all_coefficients_df.to_csv('data_hakaton1_with_coefficients.csv', index=False)



# import pandas as pd
# import random

# sales_data = pd.read_csv('data_hakaton1.csv')

# # Преобразование столбца Sale_Date в формат datetime
# sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# def multiply_with_random():
#     random_factor = random.uniform(0.1, 0.9)
#     return random_factor

# # Функция для расчета коэффициента спроса и цены за месяц
# def calculate_coefficients(data, product_name):
#     # Фильтруем данные по имени продукта и году
#     filtered_data = data[data['Product_Name'] == product_name]
#     years = filtered_data['Sale_Date'].dt.year.unique()  # Получаем уникальные года продаж
    
#     # Список для хранения данных коэффициентов и средних цен
#     coefficients_data = []

#     # Расчет коэффициентов для каждого года
#     for year in years:
#         year_data = filtered_data[filtered_data['Sale_Date'].dt.year == year]
        
#         # Расчет среднего спроса за год
#         total_demand_year = year_data['Quantity_Sold'].sum()
#         average_demand_year = total_demand_year / 12
        
#         # Расчет среднего скользящего среднего цены за месяц
#         rolling_average_price = year_data['Product_Cost'].rolling(window=3, min_periods=1).mean()  # Пример скользящего среднего с окном 3
        
#         # Расчет коэффициента спроса и цены за месяц
#         for month, average_price in zip(year_data['Sale_Date'].dt.month, rolling_average_price):
#             month_data = year_data[year_data['Sale_Date'].dt.month == month]
#             demand_coefficient = month_data['Quantity_Sold'].sum() / average_demand_year
            
#             # Логика для нового столбца
#             condition = (demand_coefficient > average_demand_year) & (average_price < rolling_average_price.mean())
#             new_column_value = 1 if condition else 0
            
#             coefficients_data.append({
#                 'Product_Name': product_name,
#                 'Year': year,
#                 'Month': month,
#                 'Demand_Coefficient': demand_coefficient * multiply_with_random(),
#                 'Average_Price': average_price,  # Добавляем скользящее среднее в данные
#                 'New_Column_Name': new_column_value,  # Добавляем новый столбец с логикой
#             })

#     return pd.DataFrame(coefficients_data)

# # Расчет коэффициентов для всех продуктов
# all_coefficients_df = pd.DataFrame()
# unique_products = sales_data['Product_Name'].unique()
# for product_name in unique_products:
#     coefficients_df = calculate_coefficients(sales_data, product_name)
#     all_coefficients_df = pd.concat([all_coefficients_df, coefficients_df])

# # Сохранение данных в CSV файл
# all_coefficients_df.to_csv('data_hakaton1_with_coefficients.csv', index=False)



# Загрузка данных из файлов
sales_data = pd.read_csv('data_hakaton1.csv')
coefficients_data = pd.read_csv('data_hakaton1_with_coefficients.csv')

# Преобразование столбца Sale_Date в формат datetime
sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])
coefficients_data['Year'] = coefficients_data['Year'].astype(str)
coefficients_data['Month'] = coefficients_data['Month'].astype(str)

# Объединение данных по условиям Product_Name, Year и Month
merged_data = pd.merge(sales_data, coefficients_data, 
                       left_on=['Product_Name', sales_data['Sale_Date'].dt.year.astype(str), sales_data['Sale_Date'].dt.month.astype(str)],
                       right_on=['Product_Name', 'Year', 'Month'],
                       how='left')

# Сохранение объединенных данных в новый файл
merged_data.to_csv('merged_data_hakaton.csv', index=False)
