import numpy as np
from prettytable import PrettyTable
from scipy import integrate

A, B = 0, 1

table = PrettyTable()
table.field_names = ['N', 'Mx', 'm', 'd_1', 'Dx', 'g', 'd_2']

size_list = [int(el) for el in input("Введите размеры массивов через пробел: ").split()]

# нахождение математического ожидания
Mx = integrate.quad(lambda x: x * np.exp(x) / (np.e - 1), A, B)
Mx = Mx[0]

# нахождение дисперсии
integrate_for_Dx = integrate.quad(lambda x: x**2 * np.exp(x) / (np.e - 1), A, B)
Dx = integrate_for_Dx[0] - Mx**2

for item in range(len(size_list)):
    num_seq_np = np.random.rand(size_list[item])
    # нахождение оценки математического ожидания
    new_num_np = np.log(np.e * num_seq_np - num_seq_np + 1)
    m = new_num_np.sum() / size_list[item]
    # нахождение оценки дисперсии
    g = (np.power(new_num_np, 2).sum() / (size_list[item] - 1)) - (size_list[item] / (size_list[item] - 1)) * m**2

    table.add_row([size_list[item], Mx, m, abs(Mx - m), Dx, g, abs(Dx - g)])

print(table)