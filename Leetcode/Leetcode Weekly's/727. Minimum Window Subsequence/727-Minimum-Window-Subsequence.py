class Solution:
    def minWindow(self, s1, s2):
        m, n = len(s1), len(s2)
        q = deque()
        seen = set()
        
        for i in range(m):
            if s1[i] == s2[0]:
                q.append((i, 0))
                seen.add((i, 0))
        
        L = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                i, j = q.popleft()
                
                if j == n - 1:
                    return s1[i-L+1:i+1]
                
                next_i, next_j = i + 1, j + 1
                if next_i < m and next_j < n:
                    if s1[next_i] == s2[next_j]:
                        state = (next_i, next_j)
                    else:
                        state = (next_i, j)
                    
                    if state not in seen:
                        seen.add(state)
                        q.append(state)
            L += 1
        
        return ""