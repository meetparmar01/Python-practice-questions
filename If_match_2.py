N = int(input("Enter the limit: "))

for num in range(1, N + 1):
    if num % 5 == 0 and num % 7 == 0: 
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Fizz")
    elif num % 7 == 0:
        print("Buzz")
    else:
        print(num)