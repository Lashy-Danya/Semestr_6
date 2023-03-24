# import numpy as np
# from queue import LifoQueue
# from graphviz import Digraph

# # Задаем начальное и конечное состояния игры в восемь
# start_state = np.array([[2,8,3],[1,6,4],[7,0,5]])
# goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # Определяем функцию для проверки, достигли ли мы целевого состояния
# def is_goal(state):
#     return np.array_equal(state, goal_state)

# # Определяем функцию для нахождения следующих возможных состояний игры в восемь
# def next_states(state):
#     zero_loc = np.argwhere(state == 0)[0]
#     i, j = zero_loc[0], zero_loc[1]
#     next_states = []
#     for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#         if x >= 0 and y >= 0 and x < 3 and y < 3:
#             next_state = np.copy(state)
#             next_state[i][j], next_state[x][y] = next_state[x][y], next_state[i][j]
#             next_states.append(next_state)
#     return next_states

# # Определяем функцию для поиска решения методом перебора в глубину
# def dfs(start_state):
#     frontier = LifoQueue()
#     explored = set()
#     frontier.put(start_state)
#     graph = Digraph(comment="8 Puzzle - DFS")
#     graph.node(name=str(start_state), label=str(start_state))
#     while not frontier.empty():
#         current_state = frontier.get()
#         if is_goal(current_state):
#             return graph
#         explored.add(str(current_state))
#         for next_state in next_states(current_state):
#             if str(next_state) not in explored:
#                 graph.node(name=str(next_state), label=str(next_state))
#                 graph.edge(str(current_state), str(next_state))
#                 frontier.put(next_state)
#     return None

# # Ищем решение методом перебора в глубину
# solution = dfs(start_state)
# # print(solution)
# solution.render('game_tree_dfs')

# import numpy as np
# from graphviz import Digraph

# # Задаем исходное состояние поля
# start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])

# # Задаем целевое состояние поля
# goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # Функция проверки совпадения текущего и целевого состояний поля
# def is_goal(state):
#     return np.array_equal(state, goal_state)

# # Функция для получения всех возможных дочерних состояний поля
# def get_children(state):
#     children = []
#     zero_pos = np.argwhere(state == 0)[0]

#     # Движение вверх
#     if zero_pos[0] > 0:
#         child = np.copy(state)
#         child[zero_pos], child[zero_pos[0] - 1, zero_pos[1]] = child[zero_pos[0] - 1, zero_pos[1]], child[zero_pos]
#         children.append(child)

#     # Движение вниз
#     if zero_pos[0] < 2:
#         child = np.copy(state)
#         child[zero_pos], child[zero_pos[0] + 1, zero_pos[1]] = child[zero_pos[0] + 1, zero_pos[1]], child[zero_pos]
#         children.append(child)

#     # Движение влево
#     if zero_pos[1] > 0:
#         child = np.copy(state)
#         child[zero_pos], child[zero_pos[0], zero_pos[1] - 1] = child[zero_pos[0], zero_pos[1] - 1], child[zero_pos]
#         children.append(child)

#     # Движение вправо
#     if zero_pos[1] < 2:
#         child = np.copy(state)
#         child[zero_pos], child[zero_pos[0], zero_pos[1] + 1] = child[zero_pos[0], zero_pos[1] + 1], child[zero_pos]
#         children.append(child)

#     return children

# # Функция для реализации метода перебора в глубину
# def dfs(state, visited, path, depth, max_depth):
#     if is_goal(state):
#         return path

#     if depth == max_depth:
#         return None

#     visited.add(str(state))

#     children = get_children(state)
#     for child in children:
#         if str(child) not in visited:
#             new_path = path.copy()
#             new_path.append(child)
#             result = dfs(child, visited, new_path, depth + 1, max_depth)
#             if result is not None:
#                 return result

#     return None

# # Функция для визуализации дерева перебора с помощью библиотеки Graphviz
# def draw_graph(start, goal, path):
#     dot = Digraph(comment='8 Puzzle DFS')

#     dot.node(str(start), str(start), shape='square')
#     dot.node(str(goal), str(goal), shape='square')

#     for i in range(len(path)):
#         dot.node(str(path[i]), str(path[i]), shape='square')

#         if i == 0:
#             dot.edge(str(start), str(path[i]))
#         else:
#             dot.edge(str(path[i-1]), str(path[i]))

#         if np.array_equal(path[i], goal):
#             break

#     dot.edge(str(path[-1]), str(goal))

#     # dot.render('8puzzle_dfs', format='png', view=True)
#     dot.render('8puzzle_dfs')

# import numpy as np
# from graphviz import Digraph

# # Целевое состояние (конечная расстановка фишек)
# goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # Функция генерации возможных наследников для заданного состояния
# def generate_successors(state):
#     successors = []
#     zero_position = np.argwhere(state == 0)[0]  # Находим позицию пустой клетки
#     moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Возможные ходы (влево, вправо, вверх, вниз)
#     for move in moves:
#         new_position = zero_position + move
#         if np.all(new_position >= 0) and np.all(new_position < state.shape):  # Проверяем, что новая позиция на доске
#             new_state = state.copy()
#             new_state[zero_position[0], zero_position[1]] = state[new_position[0], new_position[1]]
#             new_state[new_position[0], new_position[1]] = 0
#             successors.append(new_state)
#     return successors

# # Функция рекурсивного поиска в глубину
# def depth_first_search(state, goal_state, visited=None):
#     if visited is None:
#         visited = set()
#     if np.array_equal(state, goal_state):
#         return []
#     visited.add(str(state))
#     for successor in generate_successors(state):
#         if str(successor) not in visited:
#             path = depth_first_search(successor, goal_state, visited)
#             if path is not None:
#                 return [successor] + path
#     return None

# # Функция визуализации дерева перебора
# def visualize_tree(start_state, goal_state):
#     graph = Digraph()
#     queue = [(start_state, 0)]
#     visited = set()
#     while queue:
#         state, depth = queue.pop(0)
#         visited.add(str(state))
#         graph.node(str(state), str(state))
#         if np.array_equal(state, goal_state):
#             # continue
#             return graph
#         for successor in generate_successors(state):
#             if str(successor) not in visited:
#                 graph.node(str(successor), str(successor))
#                 graph.edge(str(state), str(successor))
#                 queue.append((successor, depth + 1))
#     # graph.view()

# # Пример использования функций
# start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# path = depth_first_search(start_state, goal_state)
# if path is not None:
#     print('Path:', [start_state] + path)
# else:
#     print('No path found.')
# graph = visualize_tree(start_state, goal_state)
# graph.render('game_tree-dfs')


# import numpy as np
# from graphviz import Digraph

# # Функция для получения следующих возможных состояний игры
# def get_next_states(state):
#     states = []
#     zero_pos = np.argwhere(state == 0)[0] # Находим позицию нулевого элемента
#     for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Перебираем возможные ходы
#         new_pos = zero_pos + move
#         if (new_pos >= 0).all() and (new_pos < state.shape).all(): # Проверяем, что новая позиция находится в пределах игрового поля
#             new_state = state.copy()
#             new_state[zero_pos[0], zero_pos[1]] = new_state[new_pos[0], new_pos[1]]
#             new_state[new_pos[0], new_pos[1]] = 0
#             states.append(new_state)
#     return states

# # Функция для создания графического отображения графа перебора
# def create_graph(states):
#     graph = Digraph()
#     for i, state in enumerate(states):
#         graph.node(str(i), label=str(state))
#         for next_state in get_next_states(state):
#             j = np.where((states == next_state).all(axis=(1, 2)))[0][0]
#             graph.edge(str(i), str(j))
#     return graph

# # Функция для поиска решения методом перебора в глубину
# def depth_first_search(state, goal_state, visited, graph):
#     visited.append(state)
#     if np.array_equal(state, goal_state):
#         return True
#     for next_state in get_next_states(state):
#         if not np.any([np.array_equal(next_state, v) for v in visited]):
#             graph.node(str(len(visited)), label=str(next_state))
#             graph.edge(str(len(visited)-1), str(len(visited)))
#             if depth_first_search(next_state, goal_state, visited, graph):
#                 return True
#     return False

# # Пример использования
# start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
# visited = [start_state]
# graph = create_graph([start_state])
# depth_first_search(start_state, goal_state, visited, graph)
# graph.render('dfs') # Сохраняем граф в файл dfs.pdf


# import numpy as np
# from graphviz import Digraph

# def dfs_iterative(start_state):
#     visited = []
#     stack = [start_state]
#     while stack:
#         state = stack.pop()
#         visited.append(state.tolist())
#         if np.array_equal(state, np.array([[1, 2, 3],[8, 0, 4],[7, 6, 5]])):
#             return visited
#         moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         zero_pos = np.argwhere(state == 0)[0]
#         for move in moves:
#             new_pos = zero_pos + np.array(move)
#             if (new_pos >= 0).all() and (new_pos < 3).all():
#                 new_state = np.copy(state)
#                 new_state[zero_pos[0], zero_pos[1]] = state[new_pos[0], new_pos[1]]
#                 new_state[new_pos[0], new_pos[1]] = 0
#                 if new_state.tolist() not in visited:
#                     stack.append(new_state)

# def draw_graph(visited):
#     g = Digraph('G')
#     for i, state in enumerate(visited):
#         g.node(str(i), str(state))
#         if i > 0:
#             g.edge(str(i-1), str(i))
#     g.render('game_tree_dfs')

# start_state = np.array([[2, 8, 3],[1, 6, 4],[7, 0, 5]])
# visited = dfs_iterative(start_state)
# draw_graph(visited)


# import numpy as np
# from graphviz import Digraph

# # Задаем начальное и конечное состояния игры
# start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# final_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # Создаем объект графа для визуализации дерева перебора
# dot = Digraph(comment='Game of Eight')

# # Рекурсивная функция для перебора состояний игры
# def dfs(state, depth):
#     # Добавляем узел в граф
#     dot.node(str(state), str(state))
    
#     # Если достигнуто конечное состояние, то возвращаем True
#     if np.array_equal(state, final_state):
#         return True
    
#     # Если достигнута максимальная глубина поиска, то возвращаем False
#     if depth == 0:
#         return False
    
#     # Ищем пустую клетку в текущем состоянии
#     zero_row, zero_col = np.argwhere(state == 0)[0]
    
#     # Пробуем переместить соседние клетки в пустую клетку
#     for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         new_row, new_col = zero_row + drow, zero_col + dcol
        
#         # Проверяем, что новая позиция находится в пределах поля
#         if 0 <= new_row < 3 and 0 <= new_col < 3:
#             # Создаем новое состояние игры с перемещенными клетками
#             new_state = np.copy(state)
#             new_state[zero_row, zero_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[zero_row, zero_col]
            
#             # Добавляем ребро в граф
#             dot.edge(str(state), str(new_state))
            
#             # Вызываем рекурсивно функцию для нового состояния игры
#             if dfs(new_state, depth - 1):
#                 return True
    
#     # Если не найдено конечное состояние, то возвращаем False
#     return False

# # Вызываем рекурсивную функцию для начального состояния игры
# dfs(start_state, 10)

# # Отображаем граф
# dot.render('game_of_eight.gv', view=True)


# import numpy as np
# from graphviz import Digraph

# # задаем начальное и конечное состояния игры
# start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# end_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # функция для поиска пути в глубину
# def dfs(state, path):
#     if np.array_equal(state, end_state):
#         return path
#     for move in get_possible_moves(state):
#         next_state = make_move(state, move)
#         if next_state is not None and next_state not in path:
#             path.append(next_state)
#             result = dfs(next_state, path)
#             if result is not None:
#                 return result
#             path.pop()
#     return None

# # функция для получения возможных ходов из текущего состояния
# def get_possible_moves(state):
#     moves = []
#     zero_pos = np.argwhere(state == 0)[0]
#     for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         next_pos = zero_pos + move
#         if np.all(next_pos >= 0) and np.all(next_pos < state.shape):
#             moves.append(move)
#     return moves

# # функция для совершения хода
# def make_move(state, move):
#     zero_pos = np.argwhere(state == 0)[0]
#     next_pos = zero_pos + move
#     if np.all(next_pos >= 0) and np.all(next_pos < state.shape):
#         next_state = state.copy()
#         next_state[zero_pos[0], zero_pos[1]] = next_state[next_pos[0], next_pos[1]]
#         next_state[next_pos[0], next_pos[1]] = 0
#         return next_state
#     else:
#         return None

# # функция для отображения графа перебора в Graphviz
# def draw_graph(graph):
#     dot = Digraph()
#     for i, node in enumerate(graph):
#         dot.node(str(i), label=str(node))
#         if i > 0:
#             dot.edge(str(i-1), str(i))
#     dot.render('graph.gv', view=True)

# # запускаем поиск в глубину
# path = dfs(start_state, [start_state])

# # выводим результаты поиска
# print('Path:')
# for state in path:
#     print(state)
# print('Number of nodes explored:', len(path))

# # отображаем граф перебора
# draw_graph(path)


import numpy as np
from graphviz import Digraph

# Задаем начальное и конечное состояния игры в восемь
start_state = np.array([[5, 1, 3], [8, 0, 2], [4, 7, 6]])
final_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# Функция для получения возможных ходов из текущего состояния
# def get_moves(state):
#     moves = []
#     zero_row, zero_col = np.where(state == 0)
#     if zero_row > 0:
#         new_state = state.copy()
#         new_state[zero_row, zero_col] = new_state[zero_row - 1, zero_col]
#         new_state[zero_row - 1, zero_col] = 0
#         moves.append(new_state)
#     if zero_row < 2:
#         new_state = state.copy()
#         new_state[zero_row, zero_col] = new_state[zero_row + 1, zero_col]
#         new_state[zero_row + 1, zero_col] = 0
#         moves.append(new_state)
#     if zero_col > 0:
#         new_state = state.copy()
#         new_state[zero_row, zero_col] = new_state[zero_row, zero_col - 1]
#         new_state[zero_row, zero_col - 1] = 0
#         moves.append(new_state)
#     if zero_col < 2:
#         new_state = state.copy()
#         new_state[zero_row, zero_col] = new_state[zero_row, zero_col + 1]
#         new_state[zero_row, zero_col + 1] = 0
#         moves.append(new_state)
#     return moves

def get_moves(state):
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

# Рекурсивная функция для перебора в глубину
def dfs(state, path, visited):
    visited.add(str(state))
    if np.array_equal(state, final_state):
        return path
    for move in get_moves(state):
        if str(move) not in visited:
            new_path = path + [move]
            result = dfs(move, new_path, visited)
            if result is not None:
                return result
    return None

# Находим оптимальное решение
visited = set()
path = [start_state]
result = dfs(start_state, path, visited)

# Отображаем дерево перебора
dot = Digraph()
for i, state in enumerate(result):
    label = f'Step {i}\n{state}'
    dot.node(str(i), label)
    if i > 0:
        dot.edge(str(i-1), str(i))
dot.render('dfs_game', format='png', view=True)
