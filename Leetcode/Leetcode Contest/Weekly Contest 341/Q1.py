class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        ans = [0,0]
        m = 0
        for i in range(len(mat)):
            x = mat[i].count(1)
            if m < x:
                ans = [i,x]
                m = x
        
        return ans