class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m==1 and n == 1:
            return 1
        q = collections.deque([(0,0,grid[0][0])])
        grid[0][0] = -1
        ans = 2
        while q:
            size = len(q)
            for _ in range(size):
                x,y,cur = q.popleft()
                for i in range(min(m-1,x+cur),x,-1):
                    if grid[i][y] == -1 or grid[i][y] == -3:
                        break
                    if i==m-1 and y == n-1:
                        return ans
                    if grid[i][y] == -1:
                        grid[i][y] = -3
                    else:
                        q.append((i,y,grid[i][y]))
                        grid[i][y] = -1
                
                for i in range(min(n-1,y+cur),y,-1):
                    if grid[x][i] == -2 or grid[x][i] == -3:
                        break
                    if x == m-1 and i == n-1:
                        return ans
                    if grid[x][i] == -2:
                        grid[x][i] = -3
                    else:
                        q.append((x,i,grid[x][i]))
                        grid[x][i] = -2
                
            ans += 1

        return -1
            
