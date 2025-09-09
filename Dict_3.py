d = {'a': 1, 'b': 2, 'c': 3}

inverted = {value: key for key, value in d.items()}

print("Inverted dictionary:", inverted)