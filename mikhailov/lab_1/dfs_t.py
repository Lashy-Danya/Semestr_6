import numpy as np
from graphviz import Digraph

# задаем начальное и целевое состояния игры
start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# задаем максимальную глубину
max_depth = 5

# создаем стек для хранения состояний игры
stack = [(start_state, 0)]

# создаем граф для отображения дерева перебора
graph = Digraph(comment='Game of Eight')

# добавляем начальное состояние в граф
graph.node(str(start_state), str(start_state))

def find_moves(state):
    moves = []
    zero_pos = np.where(state == 0)
    zero_row, zero_col = zero_pos[0][0], zero_pos[1][0]
    for row, col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = zero_row + row, zero_col + col
        if (new_row >= 0) and (new_row <= 2) and (new_col >= 0) and (new_col <= 2):
            new_state = state.copy()
            new_state[zero_row, zero_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[zero_row, zero_col]
            moves.append(new_state)
    return moves

# пока стек не пуст, извлекаем верхнее состояние и проверяем, является ли оно целевым или превышает максимальную глубину
while stack:
    curr_state, depth = stack.pop()
    if np.array_equal(curr_state, goal_state):
        print("Solution found!")
        break

    if depth >= max_depth:
        continue

    # сгенерируем все возможные следующие состояния и добавим их в стек и граф
    for new_state in find_moves(curr_state):
        if str(new_state) not in graph:
            graph.node(str(new_state), str(new_state))
        graph.edge(str(curr_state), str(new_state))
        stack.append((new_state, depth + 1))
    

# отображаем граф в формате pdf
graph.format = 'pdf'
graph.render('game_of_eight')
