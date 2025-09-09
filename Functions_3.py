s = input("Enter a string: ")

s_clean = s.replace(" ", "").lower()

if s_clean == s_clean[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")