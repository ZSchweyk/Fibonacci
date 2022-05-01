def fib(n, computed={1: 1, 2: 1}):
    if n not in computed:
        # print(f"{n} DNE")
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    # print(f"{n} E")
    return computed[n]

print(fib(1000))
# for i in range(1, 1001):
#     print(i, fib(i), sep=": ")

