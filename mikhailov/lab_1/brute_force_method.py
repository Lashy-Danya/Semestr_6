# import numpy as np
# from queue import Queue
# from graphviz import Digraph

# dot = Digraph('Graph', filename='brute_force.gv')

# # Функция для получения возможных следующих состояний игры
# def get_next_states(state):
#     zero_index = np.where(state == 0)
#     zero_row, zero_col = zero_index[0][0], zero_index[1][0]
#     next_states = []
#     for row, col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#         new_row, new_col = zero_row + row, zero_col + col
#         if (new_row >= 0) and (new_row <= 2) and (new_col >= 0) and (new_col <= 2):
#             new_state = state.copy()
#             new_state[zero_row, zero_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[zero_row, zero_col]
#             next_states.append(new_state)
#     return next_states

# # Функция для проверки, является ли состояние конечным
# def is_goal(state):
#     return np.array_equal(state, np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]))

# # Начальное состояние игры
# initial_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# dot.node(str(initial_state))
# # Создаем очередь и добавляем начальное состояние
# q = Queue()
# q.put(initial_state)
# steps = 0

# # Проходимся по всем возможным состояниям, пока не найдем конечное
# while not q.empty():
#     curr_state = q.get()
#     steps += 1
#     if is_goal(curr_state):
#         print("Решение найдено!")
#         break
#     next_states = get_next_states(curr_state)
#     for state in next_states:
#         q.put(state)
# print(steps)
# print(curr_state)

# # for item in range(q.qsize()):
# #     print(q.get())

# dot.view()

import numpy as np
from queue import Queue
from graphviz import Digraph

# исходное состояние игры
start_state = np.array([[2, 8, 3],[1, 6, 4],[7, 0, 5]])

# конечное состояние игры
goal_state = np.array([[1, 2, 3],[8, 0, 4],[7, 6, 5]])

# функция для нахождения всех возможных ходов
# def find_moves(state):
#     moves = []
#     zero_pos = np.argwhere(state == 0)[0]
#     for pos in [(0,1), (1,0), (0,-1), (-1,0)]:
#         move_pos = zero_pos + pos
#         if (move_pos >= 0).all() and (move_pos < 3).all():
#             new_state = state.copy()
#             new_state[zero_pos[0], zero_pos[1]] = new_state[move_pos[0], move_pos[1]]
#             new_state[move_pos[0], move_pos[1]] = 0
#             moves.append(new_state)
#     return moves

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

# функция для проверки, является ли состояние целевым
def is_goal(state):
    return np.array_equal(state, goal_state)

# функция для построения графа перебора
def build_graph(start_state):
    graph = Digraph()
    graph.node(str(start_state))
    queue = Queue()
    queue.put(start_state)
    visited = set([str(start_state)])
    while not queue.empty():
        state = queue.get()
        if is_goal(state):
            return graph
        for move in find_moves(state):
            if str(move) not in visited:
                visited.add(str(move))
                graph.node(str(move), str(move))
                graph.edge(str(state), str(move))
                queue.put(move)

# построение графа перебора
graph = build_graph(start_state)
graph.render('game_tree')

# реалезуй метод полного перебора для игры в восемь, результат должен быть [[1,2,3],[8,0,4],[7,6,5]] используя python и библиотеки numpy, queue и graphviz