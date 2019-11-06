fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(0,10)])

