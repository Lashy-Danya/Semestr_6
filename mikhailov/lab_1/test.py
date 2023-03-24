# import numpy as np
# import graphviz as gv

# def generate_moves(board):
#     # Генерация всех возможных ходов из текущей конфигурации игровой доски
#     moves = []
#     zero_pos = np.argwhere(board == 0)[0] # Поиск позиции пустой ячейки
#     for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#         r, c = zero_pos + (dr, dc)
#         if 0 <= r < 3 and 0 <= c < 3:
#             new_board = board.copy()
#             new_board[zero_pos[0], zero_pos[1]] = new_board[r, c]
#             new_board[r, c] = 0
#             moves.append(new_board)
#     return moves

# def dfs(board, goal, depth, visited, graph):
#     # Рекурсивная функция для выполнения поиска в глубину
#     visited.append(str(board)) # Добавляем текущую конфигурацию в список посещенных
#     if np.array_equal(board, goal):
#         return [board] # Если найдена целевая конфигурация, возвращаем путь
#     if depth == 0:
#         return None # Если достигнута максимальная глубина, возвращаем None
#     for move in generate_moves(board):
#         if str(move) not in visited:
#             # Добавляем ребро графа и рекурсивно ищем решение
#             graph.edge(str(board), str(move))
#             solution = dfs(move, goal, depth-1, visited, graph)
#             if solution is not None:
#                 return [board] + solution # Если найдено решение, добавляем текущую конфигурацию в путь
#     return None # Если ни один из ходов не приводит к решению, возвращаем None

# # Начальная и целевая конфигурации игровой доски
# start = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# # Создание графа и добавление начальной вершины
# graph = gv.Digraph()
# graph.node(str(start))

# # Выполнение поиска в глубину и отображение графа
# path = dfs(start, goal, depth=10, visited=[], graph=graph)
# if path is None:
#     print("Решение не найдено")
# else:
#     graph.view()

import numpy as np
from graphviz import Digraph

# функция для получения следующих возможных конфигураций игровой доски
def get_successors(board):
    successors = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                if i > 0:
                    new_board = board.copy()
                    new_board[i][j] = new_board[i-1][j]
                    new_board[i-1][j] = 0
                    successors.append(new_board)
                if i < 2:
                    new_board = board.copy()
                    new_board[i][j] = new_board[i+1][j]
                    new_board[i+1][j] = 0
                    successors.append(new_board)
                if j > 0:
                    new_board = board.copy()
                    new_board[i][j] = new_board[i][j-1]
                    new_board[i][j-1] = 0
                    successors.append(new_board)
                if j < 2:
                    new_board = board.copy()
                    new_board[i][j] = new_board[i][j+1]
                    new_board[i][j+1] = 0
                    successors.append(new_board)
    return successors

# функция для проверки, является ли данная конфигурация целевой
def is_goal(board):
    return np.array_equal(board, np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]))

# функция для рекурсивного поиска с ограничением глубины
def dfs(board, depth, max_depth, visited, path, graph):
    visited.add(str(board))
    if is_goal(board):
        return path
    if depth >= max_depth:
        return None
    successors = get_successors(board)
    for successor in successors:
        if str(successor) not in visited:
            path.append(successor)
            graph.edge(str(board), str(successor))
            result = dfs(successor, depth+1, max_depth, visited, path, graph)
            if result is not None:
                return result
            path.pop()
    return None

# функция для запуска алгоритма DFS с ограничением глубины
def run_dfs(board, max_depth):
    visited = set()
    path = [board]
    graph = Digraph()
    graph.node(str(board))
    result = dfs(board, 0, max_depth, visited, path, graph)
    if result is not None:
        for board in result:
            print(board)
        graph.view()
    else:
        print("No solution found within max depth.")

# пример использования функции
board = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
max_depth = 8
run_dfs(board, max_depth)
