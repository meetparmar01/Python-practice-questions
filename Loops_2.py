armstrong_numbers = []

for num in range(1, 10001):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    if num == total:
        armstrong_numbers.append(num)

print("Armstrong numbers between 1 and 10000 are:")
print(armstrong_numbers)