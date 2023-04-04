from queue import Queue
from graphviz import Digraph

# функция для проверки, является ли состояние целевым
def is_goal(state, target):
    return state[0] == target or state[1] == target

# Функция для генерации дочерних узлов
def find_moves(state, jug_1, jug_2):
    moves = []
    
    state_jug_1, state_jug_2 = state
    # Если кувшины не пусты, их можно опустошить
    if state_jug_1 > 0:
        moves.append((0, state_jug_2))
    if state_jug_2 > 0:
        moves.append((state_jug_1, 0))

    # Если кувшины не полные, их можно наполнить
    if state_jug_1 < jug_1:
        moves.append((jug_1, state_jug_2))
    if state_jug_2 < jug_2:
        moves.append((state_jug_1, jug_2))

    # if state_jug_1 > 0 and state_jug_2 < jug_2:
    #     amount_to_pour = min(state_jug_1, jug_2 - state_jug_2)
    #     moves.append((state_jug_1 - amount_to_pour, state_jug_2 + amount_to_pour))
    # if state_jug_2 > 0 and state_jug_1 < jug_1:
    #     amount_to_pour = min(state_jug_2, jug_1 - state_jug_1)
    #     moves.append((state_jug_1 + amount_to_pour, state_jug_2 - amount_to_pour))

    # Из непустого кувшина можно перелить в неполный
    if state_jug_1 != 0 and jug_2-state_jug_2 >= state_jug_1:
        moves.append((0, state_jug_2+state_jug_1))
    if state_jug_2 != 0 and jug_1-state_jug_1 >= state_jug_2:
        moves.append((state_jug_1+state_jug_2, 0))

    # Причем, если в неполном не хватит места,то оба кувшина останутся непустыми
    if state_jug_2 != 0 and 0 < jug_1-state_jug_1 < state_jug_2:
        moves.append((jug_1, state_jug_2 - (jug_1 - state_jug_1)))
    if state_jug_1 != 0 and 0 < jug_2-state_jug_2 < state_jug_1:
        moves.append((state_jug_1 - (jug_2 - state_jug_2), jug_2))

    return moves

# функция полного перебора
def bfs(jug_1, jug_2, target):
    queue = Queue()
    queue.put((0, 0))

    visited = [str((0, 0))]
    graph = Digraph()
    graph.node(str((0, 0)))
    steps = 0

    while not queue.empty():
        state = queue.get()

        if is_goal(state, target):
            print(f"Требуется шагов: {steps}")
            return graph
        steps += 1

        for move in find_moves(state, jug_1, jug_2):
            if str(move) not in visited:
                visited.append(str(move))
                graph.node(str(move))
                graph.edge(str(state), str(move))
                queue.put(move)
    
    return None

if __name__ == '__main__':
    
    jug_1, jug_2, target = 5, 4, 3

    graph = bfs(jug_1, jug_2, target)

    if graph is not None:
        graph.render('bfs_tree')
        graph.view()
    else:
        print(f"Нельзя с такими кувшинами получить {target} л.")