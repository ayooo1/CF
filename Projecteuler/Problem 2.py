def Even_Fibonacci_numbers():
    a = 35

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    r = list(fib(a))
    ret = []

    for x in r:
        if not x%2 and x < 4000000:
            ret.append(x)
    
    return sum(ret)

print(Even_Fibonacci_numbers())