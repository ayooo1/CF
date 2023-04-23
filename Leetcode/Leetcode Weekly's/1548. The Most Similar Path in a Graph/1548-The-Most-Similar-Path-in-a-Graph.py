class Solution:
    def mostSimilar(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[int]:
        m = len(targetPath)
        adj = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        temp = defaultdict(list)
        for i, name in enumerate(names):
            temp[name].append(i)
        names = temp
        dp = [[0]*n for _ in range(m)]
        if targetPath[0] in names:
            for name in names[targetPath[0]]: dp[0][name] += 1
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = max([dp[i-1][k] for k in adj[j]])
            for name in names[targetPath[i]]: dp[i][name] += 1
        ans = [0]*m
        ans[-1] = max([(x,i) for i, x in enumerate(dp[-1])])[1]
        prev = ans[-1]
        for i in range(m-2, -1, -1):
            cur = max(adj[prev], key=lambda x: dp[i][x])
            ans[i] = cur
            prev = cur
        return ans