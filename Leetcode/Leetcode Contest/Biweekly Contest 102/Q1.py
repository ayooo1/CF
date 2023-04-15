class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        ans = []
        m, n = len(grid), len(grid[0])
        
        for i in range(n):
            p = float('-inf')
            for j in range(m):
                p = max(p,len(str(grid[j][i])))
            
            ans.append(p)
        
        return ans