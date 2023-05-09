import numpy as np
from queue import Queue
from graphviz import Digraph

def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True

def solve_n_queens(n):
    solutions = []
    q = Queue()
    q.put([])
    while not q.empty():
        board = q.get()
        if len(board) == n:
            solutions.append(board)
        else:
            for i in range(n):
                if i not in board:
                    new_board = board + [i]
                    if is_valid(new_board):
                        q.put(new_board)
    return solutions

def draw_board(board):
    n = len(board)
    dot = Digraph(comment='N Queens')
    for i in range(n):
        for j in range(n):
            if j == board[i]:
                dot.node(f"{i},{j}", "Q", shape="circle", style="filled", fillcolor="gray")
            else:
                dot.node(f"{i},{j}", "", shape="circle")
    for i in range(n):
        for j in range(n):
            if i < n-1:
                dot.edge(f"{i},{j}", f"{i+1},{j}")
            if j < n-1:
                dot.edge(f"{i},{j}", f"{i},{j+1}")
    dot.render('board.gv', view=True)

solutions = solve_n_queens(8)
for solution in solutions:
    draw_board(solution)
