lst = [1, 2, 3, 4, 5, 6, 7]
target = int(input("Enter the sum of digit you want :"))

pairs = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))

print("Pairs with sum", target, ":", pairs)