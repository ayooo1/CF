from collections import Counter


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        par = {x:x for x in range(n)}
        size = {x:1 for x in range(n)}
        rank = {x:0 for x in range(n)}
        
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            r1,r2 = find(x),find(y)
            
            if r1 != r2:
                size[r1] = size[r2] = size[r1] + size[r2]
                if rank[r1] < rank[r2]:
                    par[r1] = r2
                else:
                    par[r2] = r1
                if rank[r1] == rank[r2]:
                    rank[r1] += 1
        
        def sizeOfGroup(x):
            return size[find(x)]
                
        s = set()
        c = Counter()
        for u,v in edges:
            union(u,v)

        for x,y in edges:
            c[x] += 1
            c[y] += 1

        for i in range(n):
            s.add(find(i))

        for i in range(n):
            f = find(i)
            if f not in s: continue
            if sizeOfGroup(f) != c[i]+1:
                s.remove(f)
        return len(s)
            