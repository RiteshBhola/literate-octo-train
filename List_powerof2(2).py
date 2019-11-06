import timeit
L = []
def f(n):
 return(2**n)
for i in range(0,10):
 L.append(f(i))
 

mycode="""
L = []
def f(n):
 return(2**n)
for i in range(0,10):
 L.append(f(i))
 """
t=timeit.timeit(mycode,number=10000)
print(L)
print("Time taken is:",t/10000)
  
"""
So i observed that it is not effective use function to calculate 2**x outside

"""
