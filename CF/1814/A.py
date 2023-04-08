x = int(input())


def func(x,y):
    if x % 2 == 1 and y%2 == 0:
        return "No"
    else:
        return "Yes"


for _ in range(x):
    n,k = input().split()
    print(func(int(n),int(k)))