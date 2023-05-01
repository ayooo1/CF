class UF:
    def __init__(self,n):
        self.n = n
        self.par = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
    
    def find(self,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self,x,y):
        p1,p2 = self.find(x), self.find(y)
        if p1 == p2: return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n <= 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        A,B = UF(n), UF(n)
        cnt = 0
        edges = sorted(edges, key = lambda x: -x[0])
        for typ,s,e in edges:
            if typ == 3:
                cnt += (A.union(s,e) | B.union(s,e))
            elif typ == 2:
                cnt += B.union(s,e)
            else:
                cnt += A.union(s,e)
        
        if A.isConnected() and B.isConnected():
            return len(edges) - cnt
        return -1