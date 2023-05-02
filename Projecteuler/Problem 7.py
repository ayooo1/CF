from collections import defaultdict


def st_prime():
    ret = defaultdict(int)
    num = 2
    i = 1
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    while not ret[10001]:
        if is_prime(num):
            ret[i] = num
            i += 1
        num += 1
    
    return ret[10001]

print(st_prime())