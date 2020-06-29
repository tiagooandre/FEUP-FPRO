def lost_element(s1, s2):
    if len(s1) > len(s2):
        return list(s1 - s2)[0]
    else:
        return list(s2 - s1)[0]

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))