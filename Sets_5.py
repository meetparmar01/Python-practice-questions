n = int(input("Enter a number: "))
num = n
factors = set()

for i in range(2, int(num**0.5) + 1):
    while n % i == 0:
        factors.add(i)
        n //= i

if n > 1:
    factors.add(n)

print("Prime factors:", factors)