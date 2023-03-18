import numpy as np
from scipy.stats import norm, chi2

# Задаем выборку
# sample = np.array([48, 52, 55, 60, 62, 63, 65, 68, 70, 72, 73, 75, 77, 80])
sample = np.random.normal(size=100)

# Задаем количество интервалов
k = 5

# low, high = np.min(sample), np.max(sample)
# intervals = np.linspace(low, high, k+1)
# hist, _ = np.histogram(sample, intervals)

# Рассчитываем интервалы и количество наблюдений в каждом интервале
hist, intervals = np.histogram(sample, k)
print(hist)
print(intervals)

# Рассчитываем среднее значение и стандартное отклонение
mu = np.mean(sample)
sigma = np.std(sample)
print(mu)
print(sigma)

# Рассчитываем ожидаемое количество наблюдений в каждом интервале
expected = np.zeros(k)
for i in range(k):
    expected[i] = norm.cdf(intervals[i + 1], mu, sigma) - norm.cdf(intervals[i], mu, sigma)
print(expected)
expected *= sample.size
print(expected)

# Рассчитываем статистику хи-квадрат
chi2_stat = np.sum((hist - expected) ** 2 / expected)
print(chi2_stat)

# Рассчитываем число степеней свободы
df = k - 1 - 2

# Рассчитываем критическое значение
alpha = 0.05
chi2_crit = chi2.ppf(1 - alpha, df)
print(chi2_crit)

# Определяем, отклоняем ли мы нулевую гипотезу
if chi2_stat > chi2_crit:
    print('Нулевая гипотеза отклоняется: выборка не соответствует нормальному распределению.')
else:
    print('Нулевая гипотеза не отклоняется: выборка соответствует нормальному распределению.')
