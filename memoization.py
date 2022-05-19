import time


def fib1(n, computed={1: 1, 2: 1}):
    if n not in computed:
        # print(f"{n} DNE")
        computed[n] = fib1(n-1, computed) + fib1(n-2, computed)
    # print(f"{n} E")
    return computed[n]


def fib2(n):
    values = [1, 1]
    if n > 2:
        for i in range(2, n+1):
            values.append(values[-1] + values[-2])

    return values[n-1]



n = 1000

start = time.perf_counter()
print(fib1(n))
print(time.perf_counter() - start, "seconds")

print()

start = time.perf_counter()
print(fib2(n))
print(time.perf_counter() - start, "seconds")



