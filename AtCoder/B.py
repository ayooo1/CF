n = int(input())
arr = list(map(int,input().split()))
x = int(input())

for i in range(x):
    k = list(map(int,input().split()))
    if k[0] == 2:
        print(arr[k[1]-1])
    else:
        arr[k[1]-1] = k[2]
