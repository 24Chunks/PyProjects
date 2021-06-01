lis = [
    ["S", "N", "A", "I", "L"],
    ["I", "T", "H", "M", "-"],
    ["R", "D4", "BoSS", "-", "M"],
    ["O", "L0s", "-", "By", "A"],
    ["G", "L", "A", "-", "P"],
]


def func(snail_map):
    output = []
    # Scan right
    x = 0
    y = 0
    dir = "RIGHT"
    while len(snail_map) != 0:
        if dir == "RIGHT" and snail_map:
            while len(snail_map[0]) > 0:
                output.append(snail_map[0][0])
                del snail_map[0][0]
            dir = "DOWN"
            snail_map = [i for i in snail_map if i != []]
        if dir == "DOWN" and snail_map:
            y = 0
            while y < len(snail_map):
                output.append(snail_map[y][-1])
                del snail_map[y][-1]
                y += 1
            dir = "LEFT"
            snail_map = [i for i in snail_map if i != []]
        if dir == "LEFT" and snail_map:
            x = len(snail_map[-1]) - 1
            while x >= 0:
                output.append(snail_map[-1][x])
                del snail_map[-1][x]
                x-= 1
            dir = "UP"
            x = 0
            snail_map = [i for i in snail_map if i != []]
        if dir == "UP" and snail_map:
            y = len(snail_map) - 1
            while y >= 0:
                output.append(snail_map[y][x])
                del snail_map[y][x]
                y -= 1
            dir = "RIGHT"
            y = 0
            snail_map = [i for i in snail_map if i != []]


    return output

print(func(lis))
