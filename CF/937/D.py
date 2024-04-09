import math
from collections import Counter

x = int(input())


s = set()

def bi():
    for i in range(1000):
        x = int(bin(i)[2:])
        if x < 10**5:
            s.add(x)
        else:
            return

bi()
s = sorted(list(s))
print(s)
# def isBi(n):
    




# for _ in range(x):
#     n = int(input())
#     print(isBi(n))