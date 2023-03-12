import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

U = 1.96
G = 1

N = int(input('Введите размер ряда: '))

mu = float(input('Введите мат. ожидание: '))
sigma = float(input('Введите сигму: '))

# mu, sigma = 0.0, 1.0

# x = np.random.default_rng().normal(mu, sigma, size=N)
x = np.random.normal(mu, sigma, size=N)

x_ = 1 / N * x.sum()

number_one = x_ - U * (G / np.sqrt(N))
number_two = x_ + U * (G / np.sqrt(N))

print(f'({number_one}, {number_two})')

# count, bins, ignored = plt.hist(x, bins=80, density=1, facecolor="blue", edgecolor="black")

ax = sns.histplot(x, bins=80, kde=True)
ax.lines[0].set_color('crimson')

# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title(f"Гистограмма для {N} элементов")
plt.show()

# TODO: Понять какой алгоритм нормального распределения используется в функции np.random.normal
# https://www.alphacodingskills.com/numpy/numpy-normal-distribution.php
# https://www.probabilitycourse.com/chapter4/4_2_3_normal.php
# https://towardsdatascience.com/random-sampling-with-scipy-and-numpy-part-iii-8daa212ce554