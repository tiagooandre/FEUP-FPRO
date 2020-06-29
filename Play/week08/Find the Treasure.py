def map(pos, steps):

    pos = list(pos)
    if len(steps) == 0:
        return tuple(pos)
    else:
        if steps[0] == "up":
            pos[1] += 1
        if steps[0] == "down":
            pos[1] -= 1
        if steps[0] == "left":
            pos[0] -= 1
        if steps[0] == "right":
            pos[0] += 1
    return map(pos, steps[1:])