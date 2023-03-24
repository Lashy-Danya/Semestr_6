import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

matplotlib.use('TkAgg')

conf_level = 0.05  # уровень доверия

N = int(input('Введите размер ряда: '))

mu = float(input('Введите мат. ожидание: '))
sigma = float(input('Введите сигму: '))

# mu, sigma = 0.0, 1.0

# x = np.random.default_rng().normal(mu, sigma, size=N)
array_list = np.random.normal(mu, sigma, size=N)

x_ = np.sum(array_list) / N

# вычисляем выборочную дисперсию
variance = sum([(x - x_) ** 2 for x in array_list]) / (N - 1)

# s = np.std(array_list, ddof=1)

# вычисляем выборочное стандартное отклонение
s = np.sqrt(variance)

# Вычисляем критическое значение распределения Стьюдента:
t = st.t.ppf((1 + 0.95) / 2, N - 1)

# t = (x_ - 0.05) / (s / np.sqrt(N))

number_one = round(x_ - t * (s / np.sqrt(N)), 6)
number_two = round(x_ + t * (s / np.sqrt(N)), 6)

print(f'Доверительный интервал: ({number_one}, {number_two})')

# count, bins, ignored = plt.hist(x, bins=80, density=1, facecolor="blue", edgecolor="black")

ax = sns.histplot(array_list, bins=80, kde=True)
ax.lines[0].set_color('crimson')

# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title(f"Гистограмма для {N} элементов")
plt.show()