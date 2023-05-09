import numpy as np
from scipy.stats import f_oneway

group_1 = np.array([int(el) for el in input("Введите данные 1 группы через пробел: ").split()])
group_2 = np.array([int(el) for el in input("Введите данные 2 группы через пробел: ").split()])
group_3 = np.array([int(el) for el in input("Введите данные 3 группы через пробел: ").split()])

F, p = f_oneway(group_1, group_2, group_3)

print(f'F: {F}')

if p < 0.05:
    print(f'Нулевая гипотеза отвергается')
else:
    print(f'Нулевую гипотезу не можем отвергать')

r = 3

count_1, count_2, count_3 = len(group_1), len(group_2), len(group_3)
count_all = count_1 + count_2 + count_3

sum_qwuad = np.sum(np.power(group_1, 2)) + np.sum(np.power(group_2, 2)) + np.sum(np.power(group_3, 2)) 

A_1, A_2, A_3 = np.sum(group_1), np.sum(group_2), np.sum(group_3)
A = A_1 + A_2 + A_3

Q = sum_qwuad - (1 / count_all) * np.power(A, 2)
Q_1 = (1 / count_1) * np.power(A_1, 2) + (1 / count_2) * np.power(A_2, 2) + (1 / count_3) * np.power(A_3, 2) - (1 / count_all) * np.power(A, 2)
Q_2 = Q - Q_1

F = (Q_1 / (r - 1)) / (Q_2 / (count_all - r))

# print(f'Q: {Q}')
# print(f'Q1: {Q_1}')
# print(f'Q2: {Q_2}')
# print(f'F: {F}')