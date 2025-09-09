words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

grouped = {}

for word in words:
    key = word[0]
    if key in grouped:
        grouped[key].append(word)
    else:
        grouped[key] = [word]

print("Grouped words by first letter:", grouped)