class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        lookup = {}
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                lookup[mat[i][j]] = (i,j)
        
        row = [0] * m
        col = [0] * n
        
        for index,x in enumerate(arr):
            i,j = lookup[x]
            
            row[i] += 1
            col[j] += 1
            
            if row[i] == n or col[j] == m:
                return index
        
        return -1