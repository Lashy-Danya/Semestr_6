import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# рандомные числа и построение гистограммы относительных частот

size = int(input('Введите размер ряда: '))

# x = np.random.rand(size)

x = np.random.uniform(size=size)

# plt.hist(x, bins=60, facecolor="blue", edgecolor="black", weights=np.ones_like(x) / size)
plt.hist(x, bins=70, facecolor="blue", edgecolor="black", density=True)

plt.title(f"Гистограмма относительных частот для {size} элементов")
plt.xlabel("Значения")
plt.ylabel("Относительная частота")

plt.show()