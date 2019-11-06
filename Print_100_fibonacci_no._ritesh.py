
import timeit
mysetup="import fibonacci as fib"
mycode="fib.fibonacci(100)"
t=timeit.timeit(setup=mysetup,stmt=mycode,number=10000)
print("Time taken to print 100 fibonacci numbers:",t/10000)


