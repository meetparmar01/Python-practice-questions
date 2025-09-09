s = input("Enter a string: ")
result = ""
seen = set()

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)

print("String after removing duplicates:", result)