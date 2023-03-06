import numpy as np
import copy

def get_initial():
    initial_array = np.array([int(el) for el in input("Введите последовательность чисел от 0 до 8: ").split()])
    initial_array = np.reshape(initial_array, (3, 3))
    return initial_array



initial_array = get_initial()
