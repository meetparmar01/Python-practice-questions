A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 7, 8}

result = ((A & B) | (B & C) | (C & A)) - (A & B & C)

print("Elements in exactly two sets:", result)