N = int(input("Enter number of rows: "))

triangle = []

for i in range(N):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

for i in range(N):
    print(" " * (N - i), end="") 
    print(" ".join(str(x) for x in triangle[i]))