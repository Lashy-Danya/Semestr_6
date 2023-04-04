from graphviz import Digraph
from queue import LifoQueue

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

def dfs(jug_1, jug_2, target):
    visited = [str((0, 0))]
    stack = LifoQueue()
    stack.put((0, 0))
    steps = 0

    graph = Digraph()
    graph.node(str((0, 0)))

    while not stack.empty():
        state = stack.get()

        if is_goal(state, target):
            print(f"Требуется шагов: {steps}")
            return graph
        steps += 1

        for move in find_moves(state, jug_1, jug_2):
            if str(move) not in visited:
                visited.append(str(move))
                graph.node(str(move))
                graph.edge(str(state), str(move))
                stack.put(move)

if __name__ == '__main__':
    
    jug_1, jug_2, target = 5, 4, 3

    graph = dfs(jug_1, jug_2, target)

    if graph is not None:
        graph.render('dfs_tree')
        graph.view()
    else:
        print(f"Нельзя с такими кувшинами получить {target} л.")