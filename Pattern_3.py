N = 5 

for i in range(1, N + 1, 2): 
    print(" " * ((N - i) // 2) + "*" * i)

for i in range(N - 2, 0, -2):
    print(" " * ((N - i) // 2) + "*" * i)