def min_path(path):
    i = 0
    while i < len(path)-1:
        if path[i] == "UP" and path[i+1] == "DOWN":
            del path[i+1]
            del path[i]
            i = 0

        elif path[i] == "DOWN" and path[i+1] == "UP":
            del path[i+1]
            del path[i]
            i = 0

        elif path[i] == "LEFT" and path[i+1] == "RIGHT":
            del path[i+1]
            del path[i]
            i = 0

        elif path[i] == "RIGHT" and path[i+1] == "LEFT":
            del path[i+1]
            del path[i]
            i = 0

        else:
            i += 1

    return path

print(min_path(['UP', 'DOWN', 'UP', 'LEFT', 'RIGHT']))