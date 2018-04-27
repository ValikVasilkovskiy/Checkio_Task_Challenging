def check_shallow(shallow_map):
    shallow_map = [(list(map(lambda x: x, i))) for i in shallow_map]
    for i in range(len(shallow_map)):
        for j in range(len(shallow_map[i])):
            if shallow_map[i][j] == 'X':
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        # only in map
                        if (row < 0) or (col < 0):
                            continue
                        else:
                            try:
                                if shallow_map[row][col] == '.':
                                    shallow_map[row][col] = 'S'
                            except IndexError:
                                continue
    return shallow_map
def finish_map(regional_map):
    safe_map = []
    regional_map = check_shallow(regional_map)
    def dfs(row, col):
        regional_map[row][col] = 'D'
        for i, j in [[row+1, col], [row, col+1], [row-1, col], [row, col-1]]:
            # only in map
            if (i < 0) or (j < 0):
                continue
            else:
                try:
                    if regional_map[i][j] == 'X':
                        regional_map[row][col] = 'S'
                    elif regional_map[i][j] != 'D' and regional_map[i][j] == '.':
                        dfs(i, j)
                except IndexError:
                    continue
    for i in range(len(regional_map)):
        for j in range(len(regional_map[i])):
            if regional_map[i][j] == 'D':
                dfs(i, j)
    for i in range(len(regional_map)):
        for j in range(len(regional_map[i])):
            if regional_map[i][j] == '.':
                regional_map[i][j] = 'S'
    for i in regional_map:
        safe_map.append(''.join(i))
    return safe_map

assert finish_map(("D..XX.....",
                   "...X......",
                   ".......X..",
                   ".......X..",
                   "...X...X..",
                   "...XXXXX..",
                   "X.........",
                   "..X.......",
                   "..........",
                   "D...X....D")) == ["DDSXXSDDDD",
                                      "DDSXSSSSSD",
                                      "DDSSSSSXSD",
                                      "DDSSSSSXSD",
                                      "DDSXSSSXSD",
                                      "SSSXXXXXSD",
                                      "XSSSSSSSSD",
                                      "SSXSDDDDDD",
                                      "DSSSSSDDDD",
                                      "DDDSXSDDDD"]
assert finish_map(("........",
                    "........",
                    "X.X..X.X",
                    "........",
                    "...D....",
                    "........",
                    "X.X..X.X",
                    "........",
                    "........",)) == ["SSSSSSSS",
                                      "SSSSSSSS",
                                      "XSXSSXSX",
                                      "SSSSSSSS",
                                      "DDDDDDDD",
                                      "SSSSSSSS",
                                      'XSXSSXSX',
                                      "SSSSSSSS",
                                      "SSSSSSSS"]

