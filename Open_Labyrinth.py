
def open_labyrinth(data):
    direct = []
    # start point
    row, col = 1, 1
    def dfs(row, col):
        data[row][col] = 2
        direction_dict = {'S': [row+1, col], 'N': [row-1, col], 'E': [row, col+1], 'W': [row, col-1]}
        # k - dict key
        for k, v in direction_dict.items():
            i, j = v[0], v[1]
            if i == 10 and j == 10:
                direct.append(k)
                direct.append('end')
            else:
                if data[i][j] != 2 and data[i][j] == 0:
                    direct.append(k)
                    dfs(i, j)
        
    dfs(row, col)
    return ''.join(direct[0:direct.index('end')])

print(open_labyrinth([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))




