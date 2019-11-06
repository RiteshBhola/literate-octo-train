import timeit
L = []

for i in range(0,10):
 L.append(2**i)
 
print(L)
mycode="""
L = []
for i in range(0,10):
 L.append(2**i)
 """
t=timeit.timeit(mycode,number=10000)

print(t/10000)
  


