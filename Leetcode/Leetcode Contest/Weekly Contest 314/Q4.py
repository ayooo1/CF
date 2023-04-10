'''

3d dp where we want to count the number of paths to a square and the 3 dimension comes from the remainder.
So each square will have how many paths to that square  for each remainder.

'''

class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n, mod = len(grid), len(grid[0]), int(1e9+7)
        if m == 1 and n == 1: return int(not grid[0][0]%k)
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        dp[-1][-1][grid[-1][-1]%k] = 1
        for offset in range(1, n):
            i, j = m-1, n-1-offset
            while i >= 0 and j < n:
                if i != m-1:
                    for l in range(k):
                        dp[i][j][(l+grid[i][j])%k]+=dp[i+1][j][l]
                        dp[i][j][(l+grid[i][j])%k]%=mod
                if j != n-1:
                    for l in range(k):
                        dp[i][j][(l+grid[i][j])%k]+=dp[i][j+1][l]
                        dp[i][j][(l+grid[i][j])%k]%=mod
                i-=1
                j+=1
        for offset in range(1, m):
            i, j = m-1-offset, 0
            while i >= 0 and j < n:
                if i != m-1:
                    for l in range(k):
                        dp[i][j][(l+grid[i][j])%k]+=dp[i+1][j][l]
                        dp[i][j][(l+grid[i][j])%k]%=mod
                if j != n-1:
                    for l in range(k):
                        dp[i][j][(l+grid[i][j])%k]+=dp[i][j+1][l]
                        dp[i][j][(l+grid[i][j])%k]%=mod
                i-=1
                j+=1
        return dp[0][0][0]