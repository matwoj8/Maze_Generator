class Node():
    def __init__(self, left = False, up = False, right = False, down = False, position = None, n = None, m = None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.position = position
        self.n = n
        self.m = m

        self.left_neighbor = (position[0], position[1] - 1) if position[1] != 0 else None
        self.right_neighbor = (position[0], position[1] + 1) if position[1] != n - 1 else None
        self.up_neighbor = (position[0] - 1, position[1]) if position[0] != 0 else None
        self.down_neighbor = (position[0] + 1, position[1]) if position[0] != m - 1 else None

        self.visited = False

def find_visited_neighbour(board, node):
    if node.left_neighbor and board[node.left_neighbor].visited: return node.left_neighbor, 0
    elif node.up_neighbor and board[node.up_neighbor].visited: return node.up_neighbor, 1
    elif node.right_neighbor and board[node.right_neighbor].visited: return node.right_neighbor, 2
    elif node.down_neighbor and board[node.down_neighbor].visited: return node.down_neighbor, 3
    else: return None


def find_all_nonvisited_neighbours(board, node):
    neighbours = []
    if node.left_neighbor and board[node.left_neighbor].visited == False:
        neighbours.append((node.left_neighbor, 0))
    if node.right_neighbor and board[node.right_neighbor].visited == False:
        neighbours.append((node.right_neighbor, 2))
    if node.up_neighbor and board[node.up_neighbor].visited == False:
        neighbours.append((node.up_neighbor, 1))
    if node.down_neighbor and board[node.down_neighbor].visited == False:
        neighbours.append((node.down_neighbor, 3))
    return neighbours

def actualize_neighbours(node1, node2, option):
    if option == 0:
        node1.left = True
        node2.right = True
    elif option == 1:
        node1.up = True
        node2.down = True
    elif option == 2:
        node1.right = True
        node2.left = True
    elif option == 3:
        node1.down = True
        node2.up = True