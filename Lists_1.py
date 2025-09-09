lst = [1, 2, 3, 4, 5]
k = int(input("Enter the number of rotations:"))

n = len(lst)

for _ in range(k):
    last = lst[-1] 
    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last

print("List after rotation:", lst)