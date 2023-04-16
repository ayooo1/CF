'''

TREE DP

'''

from functools import cache


class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        counter = [0]*n
        def path(start, end):
            counter[start]+=1
            seen.add(start)
            if start == end:
                return 1
            for nei in adj[start]:
                if nei in seen: continue
                if path(nei, end):
                    return 1
            counter[start]-=1
            return 0
        for start, end in trips:
            seen = set()
            path(start, end)
        price = [price[i]*counter[i] for i in range(n)]
        @cache
        def dfs(node, par):
            res = price[node]//2
            #If you do half the price of node:
            for nei in adj[node]:
                if nei == par: continue
                res+=price[nei]
                for child in adj[nei]:
                    if child == node: continue
                    res+=dfs(child, nei)
            #If you don't half the price of node:
            return min(res, price[node] + sum([dfs(nei, node) for nei in adj[node] if nei != par]))
        return dfs(0, -1)