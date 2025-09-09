N = 50

for num in range(2, N + 1):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime and num % 10 != 3:
        print(num, end=" ")