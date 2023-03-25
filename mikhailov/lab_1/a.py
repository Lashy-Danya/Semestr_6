import numpy as np
from queue import PriorityQueue
from graphviz import Digraph

# Целевое состояние игры
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# Определяем эвристическую функцию (расстояние Манхэттена)
def heuristic(current_state, goal_state):
    # Вычисляем расстояние Манхэттена между текущим состоянием и состоянием целевым
    return np.sum(np.abs(current_state - goal_state))

# функция для проверки, является ли состояние целевым
def is_goal(state):
    return np.array_equal(state, goal_state)

# Функция для генерации дочерних узлов
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

# Определяем функцию поиска A*
def a_star_search(start_state):

    graph = Digraph()
    graph.node(str(start_state), str(start_state))
    steps = 0

    queue = PriorityQueue()
    queue.put((0, [start_state.tolist()]))

    visited = []

    while not queue.empty():
        path_cost, path = queue.get()

        current_state = path[-1]
        current_state = np.array(current_state)

        if is_goal(current_state):

            print(f'Steps: {steps}')

            # for i, state in enumerate(path):
            #     graph.node(str(i), str(np.array(state)))

            # for i in range(len(path) - 1):
            #     graph.edge(str(i), str(i+1))

            return path, graph
        
        steps += 1
        
        visited.append(str(current_state))

        for move in find_moves(current_state):
            if str(move) not in visited:
                graph.node(str(move), str(move))
                graph.edge(str(current_state), str(move))

                new_path_cost = path_cost + 1
                new_heuristic = heuristic(move, goal_state)

                total_cost = new_path_cost + new_heuristic

                new_path = path + [move.tolist()]
                queue.put((total_cost, new_path))

    return None

if __name__ == '__main__':
    # Исходное состояние игры
    start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    
    path, graph = a_star_search(start_state)
    # print(path)
    if path is not None:
        graph.render('a*')
        graph.view()
    else:
        print('Решение не найдено')