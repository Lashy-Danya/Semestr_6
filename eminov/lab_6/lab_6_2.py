import numpy as np
from scipy.stats import chi2

def pearson_chi_square(data, alpha, k):
    # Оценка параметра lambda показательного распределения
    lambda_param = 1 / np.mean(data)

    # Определение границ интервалов
    intervals = np.linspace(0, np.max(data), k + 1)
    
    # Вычисление наблюдаемых частот
    observed_frequencies, _ = np.histogram(data, intervals)

    # Вычисление ожидаемых частот
    n = len(data)
    expected_frequencies = []
    for i in range(k):
        a = intervals[i]
        b = intervals[i + 1]
        expected_freq = n * (np.exp(-lambda_param * a) - np.exp(-lambda_param * b))
        expected_frequencies.append(expected_freq)

    # Вычисление статистики критерия Пирсона
    chi_square_statistic = np.sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)

    # Вычисление критического значения критерия Пирсона
    df = k - 1
    critical_value = chi2.ppf(1 - alpha, df)

    # Сравнение статистики критерия Пирсона с критическим значением
    if chi_square_statistic < critical_value:
        return True
    else:
        return False
    
# data = np.random.exponential(scale=2, size=100)
data = np.array([10.7834528, 93.61099552, 23.20354468, 11.44886688, 72.98541024, 123.4560133, 307.73221886, 70.77443892, 24.28046179, 59.30399486])
# data = np.array([2, 3, 5, 6, 1, 7, 4, 8])

# Генерация выборки из показательного распределения
# data = np.random.exponential(1, 100)

# Проверка выборки на соответствие показательному распределению
result = pearson_chi_square(data, 0.05, 5)
print(result)