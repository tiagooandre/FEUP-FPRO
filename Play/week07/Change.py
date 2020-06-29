def change(money):
    values = [2.0, 1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    coins = {}

    for value in values:
        coins[value] = int(money//value)
        money = round(money % value, 2)

    return coins