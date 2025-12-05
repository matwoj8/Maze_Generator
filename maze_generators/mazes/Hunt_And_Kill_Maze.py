from random import choice
from random import randint
from maze_generators.Maze import *
from maze_generators.converter import *

def generate_maze(m: int, n: int) -> (dict, list):
    maze = Maze(m, n)
    position= (randint(0 , m),randint(0 , n))
    maze.board[(0, 0)].visited = True
    mode = 0
    cnt = 1

    path = [position]

    while mode != 2:
        if cnt == m * n: mode = 2

        elif mode == 0:
            neighbours = find_all_nonvisited_neighbours(maze.board, maze.board[position])
            if neighbours == []:
                mode = 1
            else:
                new_position, option = choice(neighbours)
                actualize_neighbours(maze.board[position], maze.board[new_position], option)
                maze.board[new_position].visited = True
                path.append(new_position)
                position = new_position
                cnt += 1

        elif mode == 1:
            found = False
            for i in range(m):
                if found: break
                for j in range(n):
                    if maze.board[(i, j)].visited == False:
                        result = find_visited_neighbour(maze.board, maze.board[(i, j)])
                        if result:
                            position, option = result
                            new_position = (i, j)
                            actualize_neighbours(maze.board[new_position], maze.board[position], option)
                            maze.board[new_position].visited = True
                            path.append(new_position)
                            position = new_position
                            cnt += 1
                            mode = 0
                            found = True
                            break

    return maze, path

if __name__ == '__main__':
    maze, path = generate_maze(3, 3)
    new_maze = maze_convert(maze)
    print(new_maze)