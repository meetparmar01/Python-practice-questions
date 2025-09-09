text = input("Enter a string: ")

words = text.lower().split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word, count in freq.items():
    print(f"{word}: {count}")