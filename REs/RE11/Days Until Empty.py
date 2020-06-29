def days_until_empty(C, l):
    day = 0
    tank = C
    while (tank > 0):
        day += 1
        tank += l
        if (tank > C):
            tank = C
        tank -= day
    return day
print(days_until_empty(90, 3))