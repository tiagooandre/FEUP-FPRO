def calculator(expr):
    if type(expr) == int:
        return expr
    elif expr[1] == "+":
        res = calculator(expr[0]) + calculator(expr[2])
    elif expr[1] == "*":
        res = calculator(expr[0]) * calculator(expr[2])
    elif expr[1] == "-":
        res = calculator(expr[0]) - calculator(expr[2])

    return res
print(calculator())