# from graphviz import Digraph
# from time import time

# def is_valid(board, n, row, col):
#     # Check the row and column
#     for i in range(n):
#         if board[row][i] == 1 or board[i][col] == 1:
#             return False

#     # Check the diagonal
#     for i in range(n):
#         for j in range(n):
#             if (i+j) == (row+col) or (i-j) == (row-col):
#                 if board[i][j] == 1:
#                     return False

#     return True

# def solve_n_queens(n):
#     board = [[0] * n for _ in range(n)]
#     solution = []
#     found, count = backtrack(board, n, 0, solution)
#     if found:
#         length = sum(row.count(1) for row in solution)
#         p = n / count
#         print(length, count)
#         return solution, p
#     else:
#         return None, 0

# def backtrack(board, n, row, solution):
#     if row == n:
#         solution[:] = [row[:] for row in board]
#         return True, 1
    
#     count = 1
#     for col in range(n):
#         if is_valid(board, n, row, col):
#             board[row][col] = 1
#             found, c = backtrack(board, n, row+1, solution)
#             count += c
#             if found:
#                 return True, count
#             board[row][col] = 0
    
#     return False, count

# print("Полный перебор")
# n = 8
# # start = time()
# solution,p = solve_n_queens(n)
# if solution is not None:

#     for row in solution:
#         print(row)
#     print("p = " + str(p))
#     # print("required: %s" % (time() - start))
# else:
#     print("No solution found.")

import numpy as np
from graphviz import Digraph

def is_safe(board, row, col):
    # проверяем столбец
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # проверяем диагональ слева сверху
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # проверяем диагональ справа сверху
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    # если никакие из проверок не вернули False, то клетка безопасна
    return True

def solve_queens(board, row, num_queens, graph, node_parent):
    if row == num_queens:
        # если мы прошли все строки, то решение найдено
        return True
    
    for col in range(num_queens):
        if is_safe(board, row, col):
            # если клетка безопасна, ставим ферзя
            board[row][col] = 1
            
            # создаем узел графа и связываем его с родительским узлом
            graph.node(str(board))
            graph.edge(str(node_parent), str(board))
            
            # рекурсивно продолжаем поиск решения для следующей строки
            if solve_queens(board, row+1, num_queens, graph, str(board)):
                return True
            
            # если решение не было найдено, убираем ферзя и продолжаем перебор
            board[row][col] = 0
    
    # если не найдено решение, возвращаем False
    return False

if __name__ == '__main__':

    num_queens = 8

    board = np.zeros((num_queens, num_queens), dtype=int)
    
    # создаем граф
    graph = Digraph()
    
    # запускаем рекурсивную функцию поиска решения
    if solve_queens(board, 0, num_queens, graph, str(board)):
        # отображаем граф
        graph.render('brute_force_and_dfs')
        graph.view()
    else:  
        print('Решения нету')