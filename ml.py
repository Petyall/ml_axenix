import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.utils import resample

import os
import csv
import glob
import time
import zipfile
from google.colab import drive

drive.mount('/content/drive')

zip_file = '/content/drive/My Drive/Predicting_HardDrive_Failures_with_ML/new_data.zip'       # for test

with zipfile.ZipFile(zip_file, 'r') as z:
    z.extractall('/content/dataset')

print(f'[ Каталоги ] >>> \n{os.listdir()}')



def split_and_save_csv_files(path):
  import shutil
  from sklearn.model_selection import train_test_split

  filenames = glob.glob(os.path.join(path, "*.csv"))

  dfs = []

  for filename in filenames:
    dfs.append(pd.read_csv(filename))

  data = pd.concat(dfs, ignore_index=True)

  data_train, data_test = train_test_split(data, test_size=0.3, random_state=42)

  data_train.to_csv('/content/data_train.csv', index=False)
  data_test.to_csv('/content/data_test.csv', index=False)

  shutil.rmtree(path)


split_and_save_csv_files('/content/dataset')

df_train = pd.read_csv('data_train.csv').sample(frac=1).reset_index(drop=True).head(1000000)
df_test = pd.read_csv('data_test.csv').sample(frac=1).reset_index(drop=True).head(300000)

df_train.head()

df_train.describe()

df_test.head()

df_test.describe()

print(f'[ Размер тренировочной выборки ] >>> {df_train.shape}')
print(f'[ Размер тестовой выборки ] >>> {df_test.shape}')

target = 'New_Column_Name'

sns.countplot(df_train['New_Column_Name'])

"""### Балансировка набора данных"""

valid = df_train[df_train['New_Column_Name'] == 0]
failed = df_train[df_train['New_Column_Name'] == 1]

print("[ Число продажных продуктов ] >>> ", len(valid))
print("[ Число нерподажных продуктов ] >>> ", len(failed))

if len(valid) > 0:
    failed_up = resample(failed, replace=True, n_samples=len(valid), random_state=27)

else:
    print("Недостаточно данных в переменной 'valid'")

df_train = pd.concat([valid,failed_up])
df_train.New_Column_Name.value_counts()

sns.countplot(df_train['New_Column_Name'])

df_train

df_train.shape

# For the training data
df_train.isnull().sum()

features = [
    'Manufacture_Date',
    'Expiry_Date',
    'Sale_Date',
    'Quantity_Sold',
    'Product_Cost',
    'New_Column_Name',
    'Demand_Coefficient','Average_Price','Days_for_sale'
]

misc_feat = [fname for fname in df_train if fname not in features]
misc_feat

df_train.drop(misc_feat, inplace=True, axis=1)

df_train

obj = df_train.dtypes[df_train.dtypes == object ].index
obj

df_train = df_train.drop(obj,axis=1)

df_train.isnull().sum()

df_train['Product_Cost'] = df_train['Product_Cost'].fillna(0)

df_train['Quantity_Sold'] = df_train['Quantity_Sold'].fillna(0)

df_train['Demand_Coefficient'] = df_train['Demand_Coefficient'].fillna(0)

df_train['Average_Price'] = df_train['Average_Price'].fillna(0)

df_train['Days_for_sale'] = df_train['Days_for_sale'].fillna(0)

df_train['New_Column_Name'] = df_train['New_Column_Name'].fillna(0)

df_train.isnull().sum()

X_train = df_train.drop('New_Column_Name',axis=1)
Y_train = df_train['New_Column_Name']

valid_test = df_test[df_test['New_Column_Name'] == 0]
failed_test = df_test[df_test['New_Column_Name'] == 1]

print("Количество продажных продуктов:",len(valid_test))
print("Количество непродажных продуктов:",len(failed_test))

failed_up_test = resample(failed,replace=True,n_samples=len(valid),random_state=27)

df_test = pd.concat([valid_test,failed_up_test])
df_test.New_Column_Name.value_counts()

df_test.head()

df_test.shape

df_test.drop(misc_feat,inplace=True,axis=1)

df_test

df_test['Product_Cost'] = df_test['Product_Cost'].fillna(0)

df_test['Quantity_Sold'] = df_test['Quantity_Sold'].fillna(0)

df_test['Demand_Coefficient'] = df_test['Demand_Coefficient'].fillna(0)

df_test['Average_Price'] =df_test['Average_Price'].fillna(0)

df_test['New_Column_Name'] = df_test['New_Column_Name'].fillna(0)

df_test['Days_for_sale'] = df_test['Days_for_sale'].fillna(0)

df_test.isnull().sum()

X_test = df_test.drop('New_Column_Name',axis=1)

Y_test = df_test['New_Column_Name']

df_test.shape

"""## Построение модели рандомный лес:

### первая модель - используя X_test Y_test
"""

X_test.drop(['Expiry_Date', 'Manufacture_Date', 'Sale_Date'], axis=1, inplace=True)

print(X_train.columns)
print(X_test.columns)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(X_train, Y_train)

yPred = rfc.predict(X_test)

from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score, matthews_corrcoef
from sklearn.metrics import confusion_matrix

n_outliers = len(failed)
n_errors = (yPred != Y_test).sum()
print("Используемая модель: Классификатор случайного леса")

acc = accuracy_score(Y_test, yPred)
print("Точность составляет {}".format(acc))

prec = precision_score(Y_test, yPred)
print("Точность (precision) составляет {}".format(prec))

rec = recall_score(Y_test, yPred)
print("Полнота (recall) составляет {}".format(rec))

f1 = f1_score(Y_test, yPred)
print("F1-мера (F1-Score) составляет {}".format(f1))

MCC = matthews_corrcoef(Y_test, yPred)
print("Коэффициент корреляции Мэтьюса составляет {}".format(MCC))

"""### Визуализация"""

LABELS = ['Продажный', 'Непродажный']
conf_matrix = confusion_matrix(Y_test, yPred)
plt.figure(figsize=(12, 12))
sns.heatmap(conf_matrix, xticklabels=LABELS,
            yticklabels=LABELS, annot=True, fmt="d")
plt.title("Матрица ошибок")
plt.ylabel('Истинный класс')
plt.xlabel('Предсказанный класс')
plt.show()

"""### вторая модель - используя метод разделения"""

xData = X_train.values
yData = Y_train.values

from sklearn.model_selection import train_test_split

xTrain, xTest, yTrain, yTest = train_test_split(
        xData, yData, test_size = 0.2, random_state = 42)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(xTrain, yTrain)

ypred = rfc.predict(xTest)

from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score, matthews_corrcoef
from sklearn.metrics import confusion_matrix

n_outliers = len(failed)
n_errors = (ypred != yTest).sum()
print("Используемая модель: Классификатор случайного леса")

acc = accuracy_score(yTest, ypred)
print("Точность составляет {}".format(acc))

prec = precision_score(yTest, ypred)
print("Точность (precision) составляет {}".format(prec))

rec = recall_score(yTest, ypred)
print("Полнота (recall) составляет {}".format(rec))

f1 = f1_score(yTest, ypred)
print("F1-мера (F1-Score) составляет {}".format(f1))

MCC = matthews_corrcoef(yTest, ypred)
print("Коэффициент корреляции Мэтьюса составляет {}".format(MCC))



LABELS = ['Продажный', 'Непродажный']
conf_matrix = confusion_matrix(yTest, ypred)
plt.figure(figsize=(12, 12))
sns.heatmap(conf_matrix, xticklabels=LABELS,
            yticklabels=LABELS, annot=True, fmt="d")
plt.title("Матрица ошибок")
plt.ylabel('Истинный класс')
plt.xlabel('Предсказанный класс')
plt.show()

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

single_tree = rfc.estimators_[0]

plt.figure(figsize=(20, 10))
plot_tree(single_tree, filled=True, feature_names=X_train.columns, class_names=True)
plt.show()