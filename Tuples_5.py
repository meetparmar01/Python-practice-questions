t = (4, 2, 9, 1, 7)

lst = list(t)

min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

t = tuple(lst)

print("Tuple after swapping min and max:", t)