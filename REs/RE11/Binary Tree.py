def binary_tree(key, tree):
    maybeKey, value, left, right = tree
    if key == maybeKey:
        return value
    else:
        try:
            left()
            return binary_tree(key, left())
        except:
            return binary_tree(key, right())
print(binary_tree('hummer', ('aptitudes', 495, lambda: 1/0, lambda: ('roadblock', 25, lambda: ('paramedic', 211, lambda: ('bizets', 115, lambda: 1/0, lambda: ('modernizes', 848, lambda: ('lees', 937, lambda: ('gusty', 472, lambda: 1/0, lambda: ('haggles', 648, lambda: 1/0, lambda: ('jaclyns', 170, lambda: ('implication', 297, lambda: ('hummer', 561, lambda: 1/0, lambda: 1/0), lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))