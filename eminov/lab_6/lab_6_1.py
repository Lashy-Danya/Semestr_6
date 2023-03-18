import numpy as np
from scipy.stats import chi2
# Критерий согласия Пирсона равномерного распределения

# Задаем уровень значимости
alpha = 0.05

# Задаем наблюдаемые данные
data = np.random.uniform(low=0, high=1, size=100)
# data = np.random.normal(size=100)
# data = np.array([10.7834528, 93.61099552, 23.20354468, 11.44886688, 72.98541024, 123.4560133, 307.73221886, 70.77443892, 24.28046179, 59.30399486])

# Определяем количество интервалов
k = 5

# Вычисляем ожидаемые значения для каждого интервала
low, high = np.min(data), np.max(data)
intervals = np.linspace(low, high, k+1)
# наблюдения
observed, _ = np.histogram(data, bins=intervals)
print(observed)
# эксперементальные
# expected = np.ones(k) * len(data) / k
# expected = np.full(k, len(data) / k)
expected = len(data) / k * np.ones(k)
print(expected)

# Вычисляем статистику критерия Пирсона
stat = np.sum((observed - expected) ** 2 / expected)
print(stat)

# Сравниваем значение статистики с критическим значением
crit_value = np.percentile(np.random.chisquare(k-1, size=10000), (1-alpha)*100)
print(crit_value)

df = k - 1
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, df)
print(critical_value)

if stat > crit_value:
    print("Гипотеза о соответствии данных равномерному распределению отвергается")
else:
    print("Гипотеза о соответствии данных равномерному распределению не отвергается")