

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i in L:
 if(i==2**X):
  print("Found at",L.index(2**X))
  break
else:
  print(X, "not found")
  


