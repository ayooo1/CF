class Solution:
    def minIncrements(self, n, cost):
        cost, self.res = [0] + cost, 0
        def dfs(i):
            if i >= len(cost): return 0
            a, b = dfs(2 * i), dfs(2 * i + 1)
            self.res += abs(a - b)
            return cost[i] + max(a, b)
        dfs(1)
        return self.res