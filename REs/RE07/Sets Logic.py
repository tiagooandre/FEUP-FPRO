def logic(s, operations):
    s1 = s.copy()
    for key in operations:
        if key == "and":
            s1 = s1.intersection(operations[key])
        if key == "not":
            s1 = s1.symmetric_difference(operations[key])
        if key == "or":
            s1.update(operations[key])
        if key == "xor":
            s1.symmetric_difference_update(operations[key])

    return s1

print(logic({1, 2, 3, 4}, {'not': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}}))