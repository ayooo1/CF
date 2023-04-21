class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        mod = int(1e9+7)
        #i, n, mp:
        #idx of scheme, people left, profit left
        @cache
        def dfs(i, n, mp):
            if i == len(profit): return int(mp==0)
            res = 0
            p, c = profit[i], group[i]
            #How many combinations don't involve this crime
            res+=dfs(i+1, n, mp)
            #How many combinations do involve this crime
            if n >= c:
                res+=dfs(i+1, n-c, max(0, mp-p))
            return res%mod
        return dfs(0, n, minProfit)