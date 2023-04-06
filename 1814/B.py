from collections import deque

x = int(input())


def func(x,y):
    q = deque([(0,0)])
    s = set()
    moves = [(1,0),(0,1)]
    lvl = []
    turns = 1
    while q:
        size = len(q)
        n_lvl = []
        for _ in range(size):
            cx,cy = q.popleft()
            n_lvl.append([cx,cy])
            if cx == x and cy == y:
                return turns
            for dx,dy in moves:
                r=cx+dx
                c=cy+dy
                if (r,c) not in s:
                    q.append((r,c))
                    s.add((r,c))
                
                for i in range(len(lvl)):
                    for ccx,ccy in lvl[i]:
                        rr=ccx+dx*(turns-i)
                        cc=ccy+dy*(turns-i)
                        if (rr,cc) not in s:
                            q.append((rr,cc))
                            s.add((rr,cc))

        lvl.append(n_lvl)
        turns += 1
    return -1




for _ in range(x):
    i,j = input().split()
    print(func(int(i),int(j)))