import timeit
L = []
f=lambda n:2**n
for i in range(0,10):
 L.append(f(i))
 

mycode="""
L = []
f=lambda n:2**n
for i in range(0,10):
 L.append(f(i))
 """
t=timeit.timeit(mycode,number=10000)
print(L)
print("Time taken is:",t/10000)
  


