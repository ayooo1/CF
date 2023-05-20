class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        def find(x):
            if x == root[x]:
                return root[x], vals[x]

            root[x], val = find(root[x])
            vals[x] = vals[x] * val

            return root[x], vals[x]

        def union(x, y, original_weight):
            root_x, weight_x = find(x)
            root_y, weight_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]: 
                    root[root_y] = root_x
                    vals[root_y] = 1.0 / original_weight * weight_x / weight_y
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                    vals[root_x] = original_weight * weight_y / weight_x
                else:
                    root[root_x] = root_y
                    vals[root_x] = original_weight * weight_y / weight_x
                    rank[root_y] = rank[root_y] + 1

        # sum(a_2D_list, []) will flaten the 2D list. We then convert it to a set.
        nodes = set(sum(equations, []))
        root = {c: c for c in nodes}
        vals = {c: 1 for c in nodes}
        rank = {c: 1 for c in nodes}

        for (a, b), v in zip(equations, values):
            union(a, b, v)

        result = []
        for c, d in queries:
            if c in nodes and d in nodes: 
                parent_c, weight_c = find(c)
                parent_d, weight_d = find(d)
                if parent_c == parent_d:
                    result.append(weight_c / weight_d)
                else:
                    result.append(-1)
            else:
                result.append(-1)

        return result