def open_labyrinth(maze_map):
    direct = []
    direct_point = []
    # start point
    row, col = 1, 1
    def dfs(row, col):
        direct_point.append([row, col])
        check = 0
        maze_map[row][col] = 2
        direction_dict = {'S': [row+1, col], 'E': [row, col+1], 'N': [row-1, col], 'W': [row, col-1]}
        # k - dict key
        for k, v in direction_dict.items():
            i, j = v[0], v[1]

            if i == 10 and j == 10:
                direct.append(k)
                direct.append('end')
                check += 1
            else:
                if maze_map[i][j] != 2 and maze_map[i][j] == 0:
                    direct.append(k)
                    check += 1
                    dfs(i, j)
        if check == 0:
            direct.pop(-1)
            x = direct_point[direct_point.index([row, col]) - 1]
            dfs(x[0], x[1])
    dfs(row, col)
    return ''.join(direct[0 : direct.index('end')])


print(open_labyrinth([
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,1],
        [1,0,0,0,1,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,1,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]]))

print(open_labyrinth(
        [[1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,1,1,0,1,0,1,1,1,0,1],
        [1,0,1,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,1,0,1,0,0,0,1],
        [1,0,0,0,0,1,1,1,0,1,1,1],
        [1,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,1],
        [1,0,1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]]))




