import numpy as np
from queue import PriorityQueue
from graphviz import Digraph

def a_star(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {str(initial_state): None}
    cost_so_far = {str(initial_state): 0}

    while not frontier.empty():
        current_state = frontier.get()[1]

        if np.array_equal(current_state, goal_state):
            break

        for next_state in get_neighbors(current_state):
            new_cost = cost_so_far[str(current_state)] + 1
            if str(next_state) not in cost_so_far or new_cost < cost_so_far[str(next_state)]:
                cost_so_far[str(next_state)] = new_cost
                priority = new_cost + manhattan_distance(next_state, goal_state)
                frontier.put((priority, next_state))
                came_from[str(next_state)] = current_state

    return came_from, cost_so_far

def get_neighbors(state):
    neighbors = []
    zero_position = np.where(state == 0)

    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor_position = zero_position[0] + move[0], zero_position[1] + move[1]

        if 0 <= neighbor_position[0] < 3 and 0 <= neighbor_position[1] < 3:
            neighbor_state = state.copy()
            neighbor_state[zero_position], neighbor_state[neighbor_position] = \
                neighbor_state[neighbor_position], neighbor_state[zero_position]
            neighbors.append(neighbor_state)

    return neighbors

def manhattan_distance(state, goal_state):
    distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                continue
            goal_position = np.where(goal_state == state[i][j])
            distance += abs(i - goal_position[0]) + abs(j - goal_position[1])

    return distance

def create_graph(came_from):
    graph = Digraph()

    for node in came_from.keys():
        graph.node(node)

    for node, parent in came_from.items():
        if parent is not None:
            graph.edge(str(parent), node)

    return graph

initial_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

came_from, cost_so_far = a_star(initial_state, goal_state)
graph = create_graph(came_from)
graph.render('game_tree', view=True)
