def evaluate(a, x):
    return sum(list(map(lambda y: y*(x**a.index(y)), a)))
print(evaluate([1, 2, 4], 5))