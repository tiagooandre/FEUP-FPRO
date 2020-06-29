from functools import reduce

def reduce_map_filter(args):
    op, f, args = args
    if type(args) == type(()):
        args = reduce_map_filter(args)
    if op == "map":
        return list(map(f, args))
    if op == "filter":
        return list(filter(f, args))
    if op == "reduce":
        return reduce(f, args)
print(reduce_map_filter(('map', lambda x: 2*x, [1, 2, 3])))