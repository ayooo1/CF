from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        d = defaultdict(list)

        for i, (u,v) in enumerate(equations):
            d[u].append((v,values[i]))
            d[v].append((u, 1/values[i]))
        
        
        ans = []


        for s,e in queries:
            if s == e:
                if s not in d:
                    ans.append(float(-1))
                    continue
                else:
                    ans.append(float(1))

            else:
                q = deque([(s,1)])
                seen = set()
                hasAnswer = False

                while q:
                    cur,val = q.popleft()
                    if cur == e:
                        ans.append(val)
                        hasAnswer = True
                    
                    for node,v in d[cur]:
                        if node not in seen:
                            q.append((node,val*v))
                            seen.add(node)
                if not hasAnswer:
                    ans.append(float(-1))
        
        return ans