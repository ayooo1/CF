x = int(input())

def func(x,y):
    ans = 10**10
    for k in range(1,10**5):
        ans = min((x-1)//k+(y-1)//k+k+1,ans)
    return ans

for _ in range(x):
    i,j = map(int,input().split())
    print(func(int(i),int(j)))