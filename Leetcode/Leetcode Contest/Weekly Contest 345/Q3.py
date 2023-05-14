class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        moves = [(-1,1),(1,1),(0,1)]
        m,n = len(grid),len(grid[0])
        dp = {}
        def dfs(i,j):
            if i==m and j == n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            a = 0
            
            for dx,dy in moves:
                r = i+dx
                c = j+dy
                
                if -1<r<m and -1<c<n and grid[r][c] > grid[i][j]:
                    a = max(1 + dfs(r,c),a)
            dp[(i,j)] = a
            return a

        ans = 0
        for idx in range(m):
            ans = max(dfs(idx,0),ans)
        return ans