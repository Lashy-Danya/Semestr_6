import numpy as np
import statistics

# равномерное распределение

size = int(input('Введите размер ряда: '))

# num_seq_np = np.random.rand(size)
# num_seq_np = np.random.sample(size)

num_seq_np = np.random.random_sample(size)

# Расчет медианы
median_ = np.median(num_seq_np)
print(f'Медиана ряда: {median_}')

# Нахождение моды

# vals, counts = np.unique(num_seq_np, return_counts=True)
# mode_value = np.argwhere(counts == np.max (counts))
# print(f'Мода/ы ряда: {vals[mode_value].flatten().tolist()}')
# print(f'Встречается в ряде: {np.max (counts)} раза')

mode_ = statistics.mode(num_seq_np)
print(f'Мода {mode_}')

# Выборочно средняя
mean_ = np.nanmean(num_seq_np)
print(f'Выборочно средняя ряда: {mean_}')

# Размах
span_ = np.amax(num_seq_np) - np.amin(num_seq_np)
print(f'Размах ряда: {span_}')

# Выборочная дисперсия
sample_variance = num_seq_np.var(ddof=1)
print(f'Выборочная дисперсия: {sample_variance}')