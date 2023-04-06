x = int(input())
def func(sx:int,sy:int,ex:int,ey:int,n:int):
    ring1 = min(sx,n-1-sx,sy,n-1-sy)
    ring2 = min(ex,n-1-ex,ey,n-1-ey)
    return abs(ring1-ring2)

for _ in range(x):
    n,startx,starty,endx,endy = (int(x) for x in input().split())
    print(func(startx-1,starty-1,endx-1,endy-1,n))