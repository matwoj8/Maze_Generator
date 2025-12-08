from maze_generators.Node import Node


class Cell(Node):
    def __init__(self, node: Node, size: int, x:int, y:int) -> None:
        super().__init__(
            left=node.left,
            right=node.right,
            up=node.up,
            down=node.down,
            position=node.position,
            n=node.n,
            m=node.m
        )
        self.visited = False

        self.size = size
        self.xpos = node.position[1]*self.size+x
        self.ypos = node.position[0]*self.size+y
        self.characters = []

        # linki do sąsiednich Cell
        self.left_cell = None
        self.right_cell = None
        self.up_cell = None
        self.down_cell = None

        #wspolrzedne
        self.row = node.position[0]
        self.col = node.position[1]





