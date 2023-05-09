import numpy as np

# Ввод данных
N = int(input('Введите размер для выборки x: '))
M = int(input('Введите размер для выборки y: '))

sigma = float(input('Введите сигму (дисперсия): '))
mu_x = float(input('Введите мат. ожидание для выборки x: '))
mu_y = float(input('Введите мат. ожидание для выборки y: '))

array_x = np.random.normal(mu_x, sigma, size=N)
array_y = np.random.normal(mu_y, sigma, size=M)

# Вычисление среднего значения каждого ряда
mean_x = np.mean(array_x)
mean_y = np.mean(array_y)

# Вычисление несмещенной оценки
# s_x_square = np.sum((np.power(array_x - mean_x, 2))) / (len(array_x) - 1)
# s_y_square = np.sum((np.power(array_y - mean_y, 2))) / (len(array_y) - 1)

s_x_square = (np.power(array_x - mean_x, 2)).sum() / (len(array_x) - 1)
s_y_square = (np.power(array_y - mean_y, 2)).sum() / (len(array_y) - 1)

# s_x_square = (np.abs(array_x - mean_x)).sum() / (len(array_x) - 1)
# s_y_square = (np.abs(array_y - mean_y)).sum() / (len(array_y) - 1)

# Вычисление s в квадрате
s_square = ((N - 1) * s_x_square + (M - 1) * s_y_square) / (len(array_y) + len(array_x) - 2)
s = np.sqrt(s_square)

# Вычисление z значения
z = ((mean_x - mean_y) / s) * np.sqrt((len(array_y) * len(array_x)) / (len(array_y) + len(array_x)))

print(f'Статистический критерий: {round(z, 8)}')