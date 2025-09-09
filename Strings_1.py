def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        rest = left + right
        permute(rest, answer + ch)

string = input("Enter a string: ")
print("Permutations are:")
permute(string)