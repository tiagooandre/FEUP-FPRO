def my_key(item):
    some = -sum(item[2])
    return (some, item[0], item[1])


def sort_grades(records):
    records = sorted(records, key = my_key, reverse=False)
    return tuple(records)

print(sort_grades((('João', 'up20186042', (90, 87)), ('Ana', 'up20186040', (90, 90)), ('José', 'up20186063', (70, 90)), ('Ana', 'up20186061', (90, 90)), ('Tiago', 'up20186070', (100, 90)))))