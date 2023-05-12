class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        def dfs(i):
            if i >= n:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(questions[i][0]+dfs(i+questions[i][1]+1), dfs(i+1))
            
            return dp[i]

        dp = {}
        return dfs(0)