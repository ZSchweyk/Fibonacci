def fib(n, computed={1: 1, 2: 1}):
     if n not in computed:
         computed[n] = fib(n-1, computed) + fib(n-2, computed)

     return computed[n]


for i in range(1, 1001):
    print(i, fib(i), sep=": ")

