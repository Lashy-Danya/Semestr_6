import numpy as np
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['N', 'Mx', 'm', 'd_1', 'Dx', 'g', 'd_2']

size_list = [int(el) for el in input("Введите размеры массивов через пробел: ").split()]

x_list = np.array([int(el) for el in input("Введите массив X через пробел: ").split()])
p_list = np.array([float(el) for el in input("Введите массив P через пробел: ").split()])
p_list_copy = np.insert(p_list, 0, 0)

n_list = np.zeros(len(x_list))

# нахождение математического ожидания дискретных случайных величин
Mx = (x_list * p_list).sum()

# нахождение дисперсии дискретных случайных величин
Dx = (p_list * np.power(x_list, 2)).sum() - Mx**2

for item in range(len(size_list)):

    list_np = np.random.rand(size_list[item])

    for el in range(size_list[item]):
        min_p = 0
        for i in range(len(x_list)):
            min_p = min_p + p_list_copy[i]
            if min_p <= list_np[el] < (min_p + p_list_copy[i + 1]):
                n_list[i] += 1

    print(n_list)

    m = (x_list * n_list).sum() / size_list[item]

    g = ((x_list * x_list * n_list).sum() / size_list[item]) - m**2

    n_list = np.zeros(len(x_list))

    table.add_row([size_list[item], Mx, m, abs(Mx - m), Dx, g, abs(Dx - g)])

print(table)