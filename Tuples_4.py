t = (1, 2, 3, 2, 4, 1, 5, 2)

freq = {}

for item in t:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

for item, count in freq.items():
    if count > 1:
        print(f"{item} occurs {count} times")