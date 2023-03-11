import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

N = int(input('Введите размер ряда: '))
mu, sigma = 0.0, 1.0

# x = np.random.default_rng().normal(mu, sigma, size=N)
x = np.random.normal(mu, sigma, size=N)

x_ = 1 / N * x.sum()

u = 1.96
g = 1

number_one = x_ - u * (g / np.sqrt(N))
number_two = x_ + u * (g / np.sqrt(N))

print(f'({number_one}, {number_two})')

# count, bins, ignored = plt.hist(x, bins=80, density=1, facecolor="blue", edgecolor="black")

sns.histplot(x, bins=80, kde=True)

# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title(f"Гистограмма для {N} элементов")
plt.show()

# TODO: Понять какой алгоритм нормального распределения используется в функции np.random.normal
# https://www.alphacodingskills.com/numpy/numpy-normal-distribution.php
# https://www.probabilitycourse.com/chapter4/4_2_3_normal.php
# TODO: Переделать программу для ввода мат. ожидания и сигмы с клавиатуры