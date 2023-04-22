class Solution:
    def minInsertions(self, s: str) -> int:
        t=s[::-1]
        n=len(s)
        dp=[[0]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[-1][-1]