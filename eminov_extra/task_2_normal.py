import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# нормальное распределение и построение гистограммы

size = int(input('Введите размер ряда: '))

# mu – параметр, определяющий среднее значение
# sigma – параметр, который определяет стандартное отклонение
mu, sigma = 0, 0.3

np.random.seed(0)
# x = np.random.normal(mu, sigma, size=size)
x = np.random.default_rng().normal(mu, sigma, size=size)

# plt.hist(x, bins=20, density = 1, facecolor="blue", alpha=0.5)
# count, bins, ignored = plt.hist(x, 30, density=True)

count, bins, ignored = plt.hist(x, bins=80, density=1, facecolor="blue", edgecolor="black")

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.title(f"Гистограмма для {size} элементов")
plt.show()