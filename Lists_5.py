lst = [1, 2, None, 3, 2, None, 4, 1, 5]

result = []
seen = set()

for item in lst:
    if item is not None and item not in seen:
        result.append(item)
        seen.add(item)

print("List after removing None and duplicates:", result)