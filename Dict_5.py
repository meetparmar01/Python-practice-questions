d = {'a': 10, 'b': 35, 'c': 25, 'd': 40}

max_key = max(d, key=d.get)

print("Key with the highest value:", max_key)