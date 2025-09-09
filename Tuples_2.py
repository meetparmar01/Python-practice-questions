tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)))

print("Element-wise sum:", result)