def finish_map(regional_map):
    regional_map = [(list(map(lambda x: x, i))) for i in regional_map]
    def dfs(row, col):
        check = 0
        regional_map[row][col] = 'D'
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # only in map
                if (i < 0) or (j < 0):
                    continue
                else:
                    try:
                        if regional_map[i][j] == 'X':
                            regional_map[row][col] = 'S'
                            check += 1
                        elif regional_map[i][j] != 'D' and regional_map[i][j] == '.':
                            dfs(i, j)
                    except IndexError:
                        continue

    for i in range(len(regional_map)):
        for j in range(len(regional_map[i])):
            if regional_map[i][j] == 'D':
                dfs(i, j)
    for i in regional_map:
        print(''.join(i))

finish_map(("D..XX.....",
            "...X......",
            ".......X..",
            ".......X..",
            "...X...X..",
            "...XXXXX..",
            "X.........",
            "..X.......",
            "..........",
            "D...X....D"))
