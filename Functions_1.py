def gcd_lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    
    lcm = (a * b) // gcd
    return gcd, lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd, lcm = gcd_lcm(a, b)
print("GCD:", gcd)
print("LCM:", lcm)