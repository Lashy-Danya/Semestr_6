import numpy as np
from scipy import stats

# Генерируем случайную выборку из показательного распределения
lambda_param = 2
sample_size = 100
sample = np.random.exponential(scale=1/lambda_param, size=sample_size)

# Вычисляем среднее значение выборки
sample_mean = np.mean(sample)

# Вычисляем параметр lambda показательного распределения
lambda_estimate = 1 / sample_mean
print(lambda_estimate)

# Определяем интервалы для категорий
n_intervals = 5
interval_size = np.max(sample) / n_intervals
intervals = [i * interval_size for i in range(n_intervals + 1)]
print(sample.min())
print(intervals)

# Определяем ожидаемые значения для каждой категории
n_expected = [sample_size * stats.expon.cdf(intervals[i + 1], scale=1/lambda_estimate) - 
              sample_size * stats.expon.cdf(intervals[i], scale=1/lambda_estimate) for i in range(n_intervals)]
print(n_expected)

# Определяем наблюдаемые значения для каждой категории
n_observed, _ = np.histogram(sample, intervals)
print(n_observed)

# Вычисляем статистику хи-квадрат
chi2_stat = np.sum((n_observed - n_expected) ** 2 / n_expected)

# Определяем количество степеней свободы и критическое значение хи-квадрат распределения
df = n_intervals - 1
alpha = 0.05
chi2_crit = stats.chi2.ppf(q=1-alpha, df=df)

# Сравниваем вычисленное значение хи-квадрат со значением критической области
if chi2_stat < chi2_crit:
    print("Нулевая гипотеза принимается (данные соответствуют показательному распределению)")
else:
    print("Нулевая гипотеза отвергается (данные не соответствуют показательному распределению)")
