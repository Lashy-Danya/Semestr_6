import numpy as np
import math
import matplotlib.pyplot as plt

# Функция плотности вероятности (PDF) для нормального распределения
def normal_dist(x , mean , sd):
    prob_density = (math.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

size = int(input('Введите размер ряда: '))

x = np.linspace(1, 50, size)

mean = np.mean(x)
sd = np.std(x)

pdf = normal_dist(x, mean, sd)

print(pdf)

plt.plot(x, pdf, color = 'red')

plt.title(f"Гистограмма для {size} элементов")

plt.show()