import numpy as np
import statistics
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# Стандартное нормальное распределение

size = int(input('Введите размер ряда: '))

mu = float(input('Введите мат. ожидание: '))
sigma = float(input('Введите сигму: '))

x = np.random.normal(mu, sigma, size=size)

count, bins, ignored = plt.hist(x, bins=80, density=1, facecolor="blue", edgecolor="black")

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title(f"Гистограмма для {size} элементов")

# Медиана
median_ = np.median(x)
print(f'Медиана ряда (мат. ожидание): {median_}')

# Мода
mode_ = statistics.mode(x)
print(f'Мода {mode_}')

# Выборочно средняя
mean_ = np.nanmean(x)
print(f'Выборочно средняя ряда: {mean_}')

# Размах
span_ = np.amax(x) - np.amin(x)
print(f'Размах ряда: {span_}')

# Выборочная дисперсия
sample_variance = x.var(ddof=1)
print(f'Выборочная дисперсия: {sample_variance}')

# Вывод графика
plt.show()