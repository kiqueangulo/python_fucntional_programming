# Flatten a nested dictionary by joining the keys with "." character
def flatten_dict(dictionary):
    flat_dict = {}

    for key in dictionary.keys():
        value = dictionary[key]

        if type(value) == int:
            flat_dict[key] = value
        else:
            for inner_key in value.keys():
                flat_dict[key + '.' + inner_key] = value[inner_key]
    
    return flat_dict

# Do reverse of flatten_dict
def unflatten_dict(dictionary):
    unflat_dict = {}

    for key in dictionary.keys():
        if '.' not in key:
            unflat_dict[key] = dictionary[key]
        else:
            outter_key, inner_key = key.split('.')

            if outter_key not in unflat_dict.keys():
                unflat_dict[outter_key] = {}
                unflat_dict[outter_key][inner_key] = dictionary[key]
            else:
                unflat_dict[outter_key][inner_key] = dictionary[key]
    
    return unflat_dict

# Map a function over nested list
def treemap(Fn, items):
    for i in range(len(items)):
        if type(items[i]) != list:
            items[i] = Fn(items[i])
        else:
            items[i] = treemap(Fn, items[i])
    
    return items

example_dict = {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
example_list = [1, 2, [3, 4, [5]]]

flat_example = flatten_dict(example_dict)
map_example = treemap(lambda item: item ** 2, example_list)

print(flat_example)
print(unflatten_dict(flat_example))
print(map_example)