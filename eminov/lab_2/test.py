import math
import random

N = int(input('Сколько случайных чисел: '))
xp_count = int(input('Сколько x: '))
y = int(0)
mas_of_x = []
while y < xp_count:
    mas_of_x.append(int(input('x%s: ' % (y + 1))))
    y = y + 1
y = int(0)
mas_of_n = []
while y < xp_count:
    mas_of_n.append(0)
    y = y + 1
y = int(1)
mas_of_p = []
mas_of_p.append(float(0))
while y < xp_count + 1:
    mas_of_p.append(float(input('p%s: ' % (y))))
    y = y + 1
y = int(0)
while y < N:
    rand_num = random.random()
    y1 = int(0)
    min_p = float(0)
    while y1 < xp_count:
        min_p = min_p + mas_of_p[y1]
        if min_p <= rand_num < (min_p + mas_of_p[y1 + 1]):
            mas_of_n[y1] = mas_of_n[y1] + 1
        y1 = y1 + 1
    y = y + 1
print(mas_of_n)
nx_sum = int(0)
y = int(0)
while y < xp_count:
    nx_sum = nx_sum + mas_of_x[y] * mas_of_n[y]
    y = y + 1
nx2_sum = int(0)
y = int(0)
while y < xp_count:
    nx2_sum = nx2_sum + mas_of_x[y] * mas_of_x[y] * mas_of_n[y]
    y = y + 1
m = 1 / N * nx_sum
g = 1 / N * nx2_sum - m * m

Mx = int(0)
y = int(0)
while y < xp_count:
    Mx = Mx + mas_of_x[y] * mas_of_p[y + 1]
    y = y + 1
px2_sum = int(0)
y = int(0)
while y < xp_count:
    px2_sum = px2_sum + mas_of_x[y] * mas_of_x[y] * mas_of_p[y + 1]
    y = y + 1
Dx = px2_sum - Mx * Mx
print('     N     |        Mx       |         m          |        delta1        |        Dx       |         g          '
      '|       delta2       |')
print('----------------------------------------------------------------------------------------------------------------'
      '---------------------')
print('{:>11}'.format(N) + '|' + '{:>17}'.format(Mx) + '|' + '{:>20}'.format(m) + '|' + '{:>22}'.format(abs(
        Mx - m)) + '|' + '{:>11}'.format(Dx) + '|' + '{:>20}'.format(g) + '|' + '{:>20}'.format(abs(Dx - g)) + '|')