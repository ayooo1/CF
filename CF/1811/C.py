x = int(input())

def func(x:int, arr:list):
    last = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = min(arr[i-1],arr[i])
    res = " ".join([str(x) for x in arr + [last]])
    
    return res

for _ in range(x):
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(func(n,lst))