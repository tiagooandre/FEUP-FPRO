def sparse_dot_product(dict1, dict2):
    res = 0
    for key in dict1:
        for key2 in dict2:
            if key == key2:
                res += int(dict1[key]) * int(dict2[key2])
    return res
print(sparse_dot_product({2: 90, 9: 80, 1: -5, 8: 7}, {2: -4, 9: 1, 1: 6}))