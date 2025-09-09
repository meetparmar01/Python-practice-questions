A = {1, 2, 3}
B = {4, 5, 6}

disjoint = True
for elem in A:
    if elem in B:
        disjoint = False
        break

if disjoint:
    print("Sets are disjoint")
else:
    print("Sets are not disjoint")