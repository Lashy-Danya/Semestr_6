from graphviz import Digraph

# функция для проверки, является ли состояние целевым
def is_goal(state, target):
    return state[0] == target or state[1] == target

# Функция для генерации дочерних узлов
def find_moves(state, jug_1, jug_2):
    moves = []
    
    state_jug_1, state_jug_2 = state
    # Если кувшины не пусты, их можно опустошить
    if state_jug_2 > 0:
        moves.append((state_jug_1, 0))
    if state_jug_1 > 0:
        moves.append((0, state_jug_2))

    # Если кувшины не полные, их можно наполнить
    if state_jug_2 < jug_2:
        moves.append((state_jug_1, jug_2))
    if state_jug_1 < jug_1:
        moves.append((jug_1, state_jug_2))

    # if state_jug_1 > 0 and state_jug_2 < jug_2:
    #     amount_to_pour = min(state_jug_1, jug_2 - state_jug_2)
    #     moves.append((state_jug_1 - amount_to_pour, state_jug_2 + amount_to_pour))
    # if state_jug_2 > 0 and state_jug_1 < jug_1:
    #     amount_to_pour = min(state_jug_2, jug_1 - state_jug_1)
    #     moves.append((state_jug_1 + amount_to_pour, state_jug_2 - amount_to_pour))

    # Из непустого кувшина можно перелить в неполный
    if state_jug_2 != 0 and jug_1-state_jug_1 >= state_jug_2:
        moves.append((state_jug_1+state_jug_2, 0))
    if state_jug_1 != 0 and jug_2-state_jug_2 >= state_jug_1:
        moves.append((0, state_jug_2+state_jug_1))

    # Причем, если в неполном не хватит места,то оба кувшина останутся непустыми
    if state_jug_1 != 0 and 0 < jug_2-state_jug_2 < state_jug_1:
        moves.append((state_jug_1 - (jug_2 - state_jug_2), jug_2))
    if state_jug_2 != 0 and 0 < jug_1-state_jug_1 < state_jug_2:
        moves.append((jug_1, state_jug_2 - (jug_1 - state_jug_1)))

    return moves

steps = 0

def dfs(state, jug_1, jug_2, target, depth, visited, path, graph):
    global steps
    visited.append(str(state))

    if is_goal(state, target):
        return path
    
    if depth == 0:
        return None
    
    steps += 1

    for move in find_moves(state, jug_1, jug_2):
        if str(move) not in visited:
            path.append(move)
            graph.edge(str(state), str(move))
            result = dfs(move, jug_1, jug_2, target, depth-1, visited, path, graph)
            if result is not None:
                return result
            path.pop()

    return None

# функция для запуска алгоритма DFS с ограничением глубины
def run_dfs(state, jug_1, jug_2, target, depth):
    visited = []
    path = [state]
    graph = Digraph()
    graph.node(str(state))
    path = dfs(state, jug_1, jug_2, target, depth, visited, path, graph)

    if path is not None:
        print(f"Требуется шагов: {steps}")
        return graph
    else:
        return None

if __name__ == '__main__':
    
    jug_1, jug_2, target = 5, 4, 3

    graph = run_dfs((0, 0), jug_1, jug_2, target, 15)

    if graph is not None:
        graph.render('dfs_tree')
        graph.view()
    else:
        print(f"Нельзя с такими кувшинами получить {target} л.")