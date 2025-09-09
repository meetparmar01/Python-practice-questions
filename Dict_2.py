dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 40}

merged = {}

for key in set(dict1) | set(dict2):
    merged[key] = dict1.get(key, 0) + dict2.get(key, 0)

print("Merged dictionary:", merged)