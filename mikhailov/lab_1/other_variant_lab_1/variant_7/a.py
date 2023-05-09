
# #В алгоритме A* мы будем использовать эвристику "Количество конфликтов", которая будет оценивать количество конфликтов между ферзями на доске. Чем меньше количество конфликтов, тем более оптимальное решение.
# #Начальным состоянием для нашего алгоритма будет пустая доска без размещенных ферзей. Далее мы будем рассматривать все возможные комбинации размещения ферзей на следующей строке доски и выбирать наилучшее решение с помощью эвристики.\\
from heapq import heappop, heappush
from time import time


def conflicts(state):
    """Вычисляет количество конфликтов на доске для данного состояния."""
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # Проверяем конфликты по горизонтали и диагоналям
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                count += 1
    return count

def heuristic(state):
    """Вычисляет эвристическую функцию для данного состояния."""
    l = len(state)
    t = 0
    for i in range(l):
        new_state = state[:i] + state[i+1:]
        new_choices = tuple(c for c in range(l) if c not in new_state)
        new_f = len(new_state) + conflicts(new_state)
        t += len(new_choices) + 1
    return l/t

def solve_n_queens(n):
    """Решает задачу N ферзей на доске N×N с использованием алгоритма A*."""
    heap = [(0, (), tuple(range(n)))] # (f, state, choices)
    total_nodes = 1  # инициализируем общее число вершин
    while heap:
        f, state, choices = heappop(heap)
        if len(state) == n:
            # вычисляем P, если достигли целевого состояния
            print(n,total_nodes)
            P = n / total_nodes
            return state, P
        for i in choices:
            new_state = state + (i,)
            new_choices = tuple(c for c in choices if c != i)
            new_f = len(new_state) + conflicts(new_state)
            heappush(heap, (new_f, new_state, new_choices))
            total_nodes += 1  # увеличиваем общее число вершин
    return None, None  # возвращаем None, если не удалось найти решение

def print_solution(state):
    """Выводит решение задачи N ферзей в заданном формате."""
    for i in range(len(state)):
        row = [0] * len(state)
        row[state[i]] = 1
        print(row)

# Пример использования
print("A*")

n = 8
start = time()
solution, P = solve_n_queens(n)
if solution:
    print_solution(solution)
    print("P =", P)
    print("required: %s" % (time() - start))
else:
    print("Нет решения.")