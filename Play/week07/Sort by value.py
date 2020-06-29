def sort_by_value(dict):
    dict_sorted = sorted(dict.items(), key=lambda x: x[1])
    return dict_sorted

print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))