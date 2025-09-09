s = input("Enter a string: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

unique_vowels = {ch for ch in s if ch in vowels}

print("Unique vowels:", unique_vowels)