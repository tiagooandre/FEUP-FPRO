def find_dtype(atuple, data_type):
    new_tuple = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            new_tuple += (i,)
    return new_tuple

print(find_dtype(('keep this?', False, 'but that', True), 'bool'))