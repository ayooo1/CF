class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(q):
            ret = grid[q[0][0]][q[0][1]]
            grid[q[0][0]][q[0][1]] = 0
            while q:
                x,y = q.popleft()
                for dx,dy in moves:
                    r = x + dx
                    c = y + dy
                    if -1<r<m and -1<c<n and grid[r][c] > 0:
                        ret += grid[r][c]
                        grid[r][c] = 0
                        q.append((r,c))
            return ret
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(dfs(deque([(i,j)])), ans)
        return ans
        