a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

match op:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        if b != 0:
            result = a / b
        else:
            result = "Error! Division by zero."
    case _:
        result = "Invalid operation."

print("Result:", result)