x = int(input())


def func(x,y):
    if x % 2 == 0:
        return "YES"

    elif (x%2==1 and y%2 == 1) or (x%2 == 0 and y%2 == 0) or (x%2==0 and y%2==1):
        return "YES"

    else:
        return "NO"


for _ in range(x):
    n,k = input().split()
    print(func(int(n),int(k)))