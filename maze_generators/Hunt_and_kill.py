from random import choice

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

def find_visited_neighbour(maze, node):
    if node.left_neighbor and maze[node.left_neighbor].visited: return node.left_neighbor, 0
    elif node.up_neighbor and maze[node.up_neighbor].visited: return node.up_neighbor, 1
    elif node.right_neighbor and maze[node.right_neighbor].visited: return node.right_neighbor, 2
    elif node.down_neighbor and maze[node.down_neighbor].visited: return node.down_neighbor, 3
    else: return None


def find_all_nonvisited_neighbours(maze, node):
    neighbours = []
    if node.left_neighbor and maze[node.left_neighbor].visited == False:
        neighbours.append((node.left_neighbor, 0))
    if node.right_neighbor and maze[node.right_neighbor].visited == False:
        neighbours.append((node.right_neighbor, 2))
    if node.up_neighbor and maze[node.up_neighbor].visited == False:
        neighbours.append((node.up_neighbor, 1))
    if node.down_neighbor and maze[node.down_neighbor].visited == False:
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

def generate_maze(m: int, n: int) -> dict:
    maze = {(i, j): Node(position = (i, j), n = n, m = m) for i in range(m) for j in range(n)}
    position= (0,0)
    maze[(0, 0)].visited = True
    mode = 0
    cnt = 1

    while mode != 2:
        if cnt == m * n: mode = 2

        elif mode == 0:
            neighbours = find_all_nonvisited_neighbours(maze, maze[position])
            if neighbours == []:
                mode = 1
            else:
                new_position, option = choice(neighbours)
                actualize_neighbours(maze[position], maze[new_position], option)
                maze[new_position].visited = True
                position = new_position
                cnt += 1

        elif mode == 1:
            found = False
            for i in range(m):
                if found: break
                for j in range(n):
                    if maze[(i, j)].visited == False:
                        result = find_visited_neighbour(maze, maze[(i, j)])
                        if result:
                            position, option = result
                            new_position = (i, j)
                            actualize_neighbours(maze[new_position], maze[position], option)
                            maze[new_position].visited = True
                            position = new_position
                            cnt += 1
                            mode = 0
                            found = True
                            break

    return maze

def maze_convert(maze):
    new_maze = {}
    for (i, j) in maze:
        new_maze[(i, j)] = set()
        if maze[(i, j)].right:
            new_maze[(i, j)].add((i, j + 1))
        if maze[(i, j)].left:
            new_maze[(i, j)].add((i, j - 1))
        if maze[(i, j)].up:
            new_maze[(i, j)].add((i - 1, j ))
        if maze[(i, j)].down:
            new_maze[(i, j)].add((i + 1, j))
    for pos in new_maze:
        new_maze[pos] = list(new_maze[pos])
    return new_maze

if __name__ == '__main__':
    maze = generate_maze(3, 3)
    new_maze = maze_convert(maze)
    print(new_maze)