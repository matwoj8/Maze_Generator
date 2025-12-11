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
        self.characters = set()

        # linki do sąsiednich Cell
        self.left_cell = None
        self.right_cell = None
        self.up_cell = None
        self.down_cell = None

        #wspolrzedne
        self.row = node.position[0]
        self.col = node.position[1]

    #zwraca liste postaci bedącą w komórckach sąsiednich,do których istnieje przejsćie
    def get_nearby_characters(self)->list:
        n_characters = list(self.characters)
        if self.right_cell is not None and self.right: n_characters.extend(self.right_cell.get_nearby_characters())
        if self.left_cell is not None and self.left: n_characters.extend(self.left_cell.characters)
        if self.up_cell is not None and self.up: n_characters.extend(self.up_cell.characters)
        if self.down_cell is not None and self.down: n_characters.extend(self.down_cell.characters)
        return n_characters





