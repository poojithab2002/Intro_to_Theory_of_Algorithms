import sys

sys.setrecursionlimit(10 ** 6) # Set the recursion limit to a higher value

direction_path = []  # List to keep track of final directions
spaces_path = []  # List to keep track of space between nodes in the maze

# Function to read the maze from an input file
def read_input_file(file_name):
    with open(file_name, 'r') as file:
        rows, cols = map(int, file.readline().split())
        maze = [file.readline().split() for _ in range(rows)]
    return maze

# Function to solve the maze using DFS
def solve_maze_dfs(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    color = []  # A matrix for colors in the maze
    direction = []  # A matrix for direction in the maze

    # Populate the color and direction matrices based on the input maze
    for i in range(rows):
        color.append([])
        direction.append([])
        for j in range(cols):
            if i == rows - 1 and j == cols - 1:
                color[i].append('O')  # for BullsEye there is no color, So keeping it 'O'
                direction[i].append('O')  # for BullsEye there is no direction, So keeping it 'O'
            else:
                c, d = maze[i][j].split('-')
                color[i].append(c)
                direction[i].append(d)
            # print(color[i][j], end="")
            # print(direction[i][j], end="  ")
        # print()

    # Recursive function to explore the maze using DFS
    def dfs(x, y, path):
        if x == rows - 1 and y == cols - 1:  # Base condition if we reach the Bulls Eye.
            # print(path)
            # Based on final path taken,
            # compute the final directions and steps/spaces taken in corresponding directions
            # for example, in path there are two adjacent elements,
            # say, (2,3) and (0,5). this means we took 2 spaces towards NE
            for i in range(0, len(path) - 1):
                # Calculate directions and spaces based on consecutive path points
                if path[i][0] == path[i + 1][0]:
                    if (path[i + 1][1] - path[i][1]) < 0:
                        direction_path.append('W')
                        spaces_path.append(abs(path[i + 1][1] - path[i][1]))
                    elif (path[i + 1][1] - path[i][1]) > 0:
                        direction_path.append('E')
                        spaces_path.append(abs(path[i + 1][1] - path[i][1]))
                elif path[i][1] == path[i + 1][1]:
                    if (path[i + 1][0] - path[i][0]) < 0:
                        direction_path.append('N')
                        spaces_path.append(abs(path[i + 1][0] - path[i][0]))
                    elif (path[i + 1][0] - path[i][0]) > 0:
                        direction_path.append('S')
                        spaces_path.append(abs(path[i + 1][0] - path[i][0]))
                else:
                    dif_x = path[i+1][0] - path[i][0]
                    dif_y = path[i+1][1] - path[i][1]
                    if dif_x < 0:
                        if dif_y < 0:
                            direction_path.append('NW')
                            spaces_path.append(abs(dif_x))
                        elif dif_y > 0:
                            direction_path.append('NE')
                            spaces_path.append(abs(dif_x))
                    elif dif_x > 0:
                        if dif_y < 0:
                            direction_path.append('SW')
                            spaces_path.append(abs(dif_x))
                        elif dif_y > 0:
                            direction_path.append('SE')
                            spaces_path.append(abs(dif_x))
            return True  # Reached the bottom-right corner So we return True
        if x == rows or y == cols:
            return False  # return false if trying to go out of the maze

        # print(x,y, visited[x][y])
        # Recursion
        c, d = maze[x][y].split('-')
        if d == 'N':
            # Explore in the north direction
            for i in range(x - 1, -1, -1):
                if (color[i][y] != color[x][y] and visited[i][y] < 1):
                    visited[i][y] += 1
                    result = dfs(i, y, path + [(i, y)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][y] -= 1  # else backtracked
        elif d == 'E':
            # Explore in the east direction
            for j in range(y + 1, cols):
                if color[x][j] != color[x][y] and visited[x][j] < 1:
                    visited[x][j] += 1
                    result = dfs(x, j, path + [(x, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[x][j] -= 1  # else backtracked
        elif d == 'S':
            # Explore in the south direction
            for i in range(x + 1, rows):
                if (color[i][y] != color[x][y] and visited[i][y] < 1):
                    visited[i][y] += 1
                    result = dfs(i, y, path + [(i, y)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][y] -= 1  # else backtracked
        elif d == 'W':
            # Explore in the west direction
            for j in range(y - 1, -1, -1):
                if color[x][j] != color[x][y] and visited[x][j] < 1:
                    visited[x][j] += 1
                    result = dfs(x, j, path + [(x, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[x][j] -= 1  # else backtracked
        elif d == 'NE':
            # Explore in the northeast direction
            i = x - 1
            j = y + 1
            while i >= 0 and j < cols:
                if color[i][j] != color[x][y] and visited[i][j] < 1:
                    visited[i][j] += 1
                    result = dfs(i, j, path + [(i, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][j] -= 1  # else backtracked
                i -= 1
                j += 1
        elif d == 'SE':
            # Explore in the southeast direction
            i = x + 1
            j = y + 1
            while i < rows and j < cols:
                if color[i][j] != color[x][y] and visited[i][j] < 1:
                    visited[i][j] += 1
                    result = dfs(i, j, path + [(i, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][j] -= 1  # else backtracked
                i += 1
                j += 1
        elif d == 'SW':
            # Explore in the southwest direction
            i = x + 1
            j = y - 1
            while i < rows and j >= 0:
                if color[i][j] != color[x][y] and visited[i][j] < 1:
                    visited[i][j] += 1
                    result = dfs(i, j, path + [(i, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][j] -= 1  # else backtracked
                i += 1
                j -= 1
        elif d == 'NW':
            # Explore in the northwest direction
            i = x - 1
            j = y - 1
            while i >= 0 and j >= 0:
                if color[i][j] != color[x][y] and visited[i][j] < 1:
                    visited[i][j] += 1
                    result = dfs(i, j, path + [(i, j)])  # call the dfs function by stepping on this location
                                                         # and including it in path
                    if result:
                        return result  # if result is true then return true
                    visited[i][j] -= 1  # else backtracked
                i -= 1
                j -= 1

        return False  # No path found

    start_node = (0, 0)
    visited[0][0] = 1
    if not dfs(0, 0, [start_node]):
        print("No Path exist")

# Function to write the solution to an output file
def write_output_file(file_name, d_list, s_list):
    with open(file_name, 'w') as file:
        moves = []
        for i in range(0, len(d_list)):
            moves.append(f"{s_list[i]}{d_list[i]}")

        file.write(" ".join(moves))

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    maze = read_input_file(input_file)
    solution = solve_maze_dfs(maze)
    write_output_file(output_file, direction_path, spaces_path)


