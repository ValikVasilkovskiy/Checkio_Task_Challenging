row, col = 1, 1
direction_dict = {'S': [row+1, col], 'N': [row-1, col], 'E': [row, col+1], 'W': [row, col-1]}
for k, v in direction_dict.items():
    print(v[0], v[1])


