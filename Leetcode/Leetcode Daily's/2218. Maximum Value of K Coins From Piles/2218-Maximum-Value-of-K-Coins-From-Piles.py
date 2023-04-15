class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        n = len(piles)

        dp = [[-1]*(k+1) for i in range(n) ]

        def dfs(i,c):
            if i == n:
                return 0
            
            if dp[i][c] != -1:
                return dp[i][c]

            dp[i][c] = dfs(i+1,c) #skip pile
            cur = 0

            for j in range(min(len(piles[i]),c)):
                cur += piles[i][j]
                dp[i][c] = max(cur + dfs(i + 1, c - j - 1), dp[i][c])
            
            return dp[i][c]


        return dfs(0,k)