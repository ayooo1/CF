from math import gcd, sqrt

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def Largest_prime_factor():
    ret = []
    num = 600851475143
    for x in range(int(sqrt(num)),0,-1):
        if num%x == 0:
            ret.append(x)
    
    for x in ret:
        if is_prime(x):
            return x
    
    return -1

print(Largest_prime_factor())
        