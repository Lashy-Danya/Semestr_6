import numpy as np
from queue import Queue
from graphviz import Digraph

# конечное состояние игры
goal_state = np.array([[1, 2, 3],[8, 0, 4],[7, 6, 5]])

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

# функция для проверки, является ли состояние целевым
def is_goal(state):
    return np.array_equal(state, goal_state)

# функция для построения графа перебора
def build_graph(start_state):
    graph = Digraph()
    steps = 0
    graph.node(str(start_state))
    queue = Queue()
    queue.put(start_state)
    visited = [str(start_state)]
    while not queue.empty():
        state = queue.get()
        if is_goal(state):
            print(f'Steps: {steps}')
            return graph
        steps += 1
        for move in find_moves(state):
            if str(move) not in visited:
                visited.append(str(move))
                graph.node(str(move), str(move))
                graph.edge(str(state), str(move))
                queue.put(move)

    return None

if __name__ == '__main__':
    # Исходное состояние игры
    start_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])

    # построение графа перебора
    graph = build_graph(start_state)
    if graph is not None:
        graph.render('game_tree')
        graph.view()
    else:
        print(f'Значение графа: {graph}')