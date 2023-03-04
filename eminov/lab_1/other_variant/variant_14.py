import numpy as np
from prettytable import PrettyTable
from scipy import integrate

A, B = 0, np.pi / 4

table = PrettyTable()
table.field_names = ['N', 'Mx', 'm', 'd_1', 'Dx', 'g', 'd_2']

size_list = [int(el) for el in input("Введите размеры массивов через пробел: ").split()]

# нахождение математического ожидания
Mx = integrate.quad(lambda x: x * 1 / (np.cos(x)**2), A, B)
Mx = Mx[0]

# нахождение дисперсии
integrate_for_Dx = integrate.quad(lambda x: x**2 * 1 / (np.cos(x)**2), A, B)
Dx = integrate_for_Dx[0] - Mx**2

for item in range(len(size_list)):
    num_seq_np = np.random.rand(size_list[item])
    # нахождение оценки математического ожидания
    new_num_np = np.sqrt(num_seq_np)
    m = new_num_np.sum() / size_list[item]
    # нахождение оценки дисперсии
    g = (np.power(new_num_np, 2).sum() / (size_list[item] - 1)) - (size_list[item] / (size_list[item] - 1)) * m**2

    table.add_row([size_list[item], Mx, m, abs(Mx - m), Dx, g, abs(Dx - g)])

print(table)