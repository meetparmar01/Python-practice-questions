ch = input("Enter a character: ")

if ch in "AEIOUaeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")