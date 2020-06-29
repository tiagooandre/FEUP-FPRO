def map(pos, steps):

    x = pos[0]
    y = pos[1]

    steps = steps.split("-")

    for i in steps:
        if i == "up":
            y += 1
        elif i == "down":
            y -= 1
        elif i == "left":
            x -= 1
        elif i == "right":
            x += 1

    return (x, y)

print(map((0, 0), "up-up-left-right-up-up"))