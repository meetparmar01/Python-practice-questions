N = int(input("Enter N: "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(f"{i*j:4}", end="") 
    print()