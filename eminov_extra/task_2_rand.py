import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# рандомные числа и построение гистограммы частот

size = int(input('Введите размер ряда: '))

# x = np.random.rand(size)

x = np.random.uniform(size=size)

plt.hist(x, facecolor="blue", bins=60, edgecolor="black")

plt.title(f"Гистограмма частот для {size} элементов")
plt.xlabel("Значения")
plt.ylabel("Частота")

plt.show()