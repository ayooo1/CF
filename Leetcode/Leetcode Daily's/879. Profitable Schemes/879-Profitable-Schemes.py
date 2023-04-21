class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        mod = int(1e9+7)
        dp = [[0]*(n+1) for _ in range(minProfit+1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(minProfit, -1, -1):
                for j in range(n-g, -1, -1):
                    dp[min(i+p, minProfit)][j+g]+=dp[i][j]
        return sum(dp[-1])%mod