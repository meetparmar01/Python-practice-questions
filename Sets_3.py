A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

diff1 = {x for x in A if x not in B}

diff2 = {x for x in B if x not in A}

sym_diff = diff1 | diff2

print("Symmetric difference:", sym_diff)