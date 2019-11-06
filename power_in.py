L = [1, 2, 4, 8, 16, 32, 64]
x = 5

if 2**x not in L:
 print(x,"Not Found")
else:
 print("Found at index",L.index(2**x))
