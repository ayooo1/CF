class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        root, size = list(range(n)), [1]*n
        def find(a):
            while root[root[a]] != root[a]: root[a] = root[root[a]]
            return root[a]
        def union(a, b):
            a, b = find(a), find(b)
            if a == b: return
            if size[b] > size[a]:
                size[b] += size[a]
                root[a] = b
            else:
                size[a] += size[b]
                root[b] = a
        res = [None]*len(queries)
        queries = sorted([queries[i] + [i] for i in range(len(queries))], key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        q = 0
        for u, v, w in edgeList:
            while q < len(queries) and queries[q][2] <= w:
                res[queries[q][3]] = find(queries[q][0]) == find(queries[q][1])
                q+=1
            union(u, v)
        while q < len(queries):
            res[queries[q][3]] = find(queries[q][0]) == find(queries[q][1])
            q+=1
        return res