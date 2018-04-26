t = ("D..XX.....",
            "...X......",
            ".......X..",
            ".......X..",
            "...X...X..",
            "...XXXXX..",
            "X.........",
            "..X.......",
            "..........",
            "D...X....D")
new_t = [(list(map(lambda x: x, i))) for i in t]


for i in new_t:
    print(i, end='\n')


