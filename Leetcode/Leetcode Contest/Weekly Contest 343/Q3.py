class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        n = len(specialRoads) + 2
        
        inf = 10**20
        dist = [inf]*n
        best = abs(start[0]-target[0]) + abs(start[1]-target[1])
        
        h = []
        heappush(h,(0,start[0],start[1],-1))
        
        while h:
            d,x,y,i = heappop(h)
            
            if i != -1 and dist[i] > d:
                continue
            
            best = min(best, abs(x-target[0]) + abs(y-target[1]) + d)
            
            for idx, (sx, sy, ex, ey, c) in enumerate(specialRoads):
                cost = d + abs(sx-x) + abs(sy-y) + c
                
                if cost < dist[idx]:
                    dist[idx] = cost
                    heappush(h,(cost,ex,ey,idx))
            
        return best