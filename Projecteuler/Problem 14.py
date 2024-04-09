def collatz(n):
    if n == 1:
        return 0
    if n%2:
        return 1 + collatz(3*n + 1)
    else:
        return 1 + collatz(n//2)
    

m = 0
ret = 0
for i in range(1,1000001,2):
    x = collatz(i)
    if x > m:
        m = x
        ret = i

print(ret)