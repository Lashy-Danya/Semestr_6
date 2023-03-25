import numpy as np
from graphviz import Digraph

# Целевое состояние игры
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

def find_moves(state):
    moves = []
    zero_pos = np.where(state == 0)
    zero_row, zero_col = zero_pos[0][0], zero_pos[1][0]
    for row, col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = zero_row + row, zero_col + col
        if (new_row >= 0) and (new_row <= 2) and (new_col >= 0) and (new_col <= 2):
            new_state = state.copy()
            new_state[zero_row, zero_col], new_state[new_row, new_col] = \
            new_state[new_row, new_col], new_state[zero_row, zero_col]
            moves.append(new_state)
    return moves

# функция для проверки, является ли состояние целевым
def is_goal(state):
    return np.array_equal(state, goal_state)

steps = 0

# функция для рекурсивного поиска с ограничением глубины
def dfs(state, depth, visited, path, graph):
    global steps
    visited.append(str(state))

    if is_goal(state):
        print(f'Steps: {steps}')
        return path
    
    if depth == 0:
        return None
    
    steps += 1

    for move in find_moves(state):
        if str(move) not in visited:
            path.append(move)
            graph.edge(str(state), str(move))
            result = dfs(move, depth-1, visited, path, graph)
            if result is not None:
                return result
            path.pop()

    return None

# функция для запуска алгоритма DFS с ограничением глубины
def run_dfs(state, depth):
    visited = []
    path = [state]
    graph = Digraph()
    graph.node(str(state))
    path = dfs(state, depth, visited, path, graph)
    
    return path, graph

if __name__ == '__main__':
    # Исходное состояние игры
    start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    
    path, graph = run_dfs(start_state, 10)

    if path is not None:
        # print(path, end='\n\n')
        graph.render('dfs')
        graph.view()
    else:
        print("Решение не найдено в пределах максимальной глубины")