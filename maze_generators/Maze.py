from maze_generators.Node import *

class Maze:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.board = {(i, j): Node(position = (i, j), n = n, m = m) for i in range(m) for j in range(n)}