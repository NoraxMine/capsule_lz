import matplotlib.pyplot as plt
import os
import datetime
import pandas as pd
import numpy as nm










df = pd.read_csv('personal_transactions.csv', header=None) # чтение файла без заголовков  # выбираем нужные столбцы
df.columns = ['Date', 'Description', 'Description', 'Transaction Type','Category','Account Name'] # присвоение имен столбцам


def logger():
    def wrapper(*args, **kwargs):
       
        df = pd.read_csv("personal_transactions.csv", usecols=[5])
        
        

        
        
    return wrapper

    
# Данные для диаграммы
a = df.value_counts()
z = int(a[0])
x = int(a[1])
c = int(a[2])
labels = [z, x, c]
sizes = [40, 30, 30]  # Доли в процентах
colors = ['gold', 'yellowgreen', 'lightcoral']  # Цвета сегментов

# Построение диаграммы
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Настройка оси для круговой диаграммы
plt.axis('equal')

# Показать диаграмму
plt.show()

logger()