def Summation_of_primes():
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    ret = []

    for i in range(2000000):
        if is_prime(i):
            ret.append(i)

    return sum(ret)

print(Summation_of_primes())