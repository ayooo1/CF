class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i+j == n-1:
                    ans += mat[i][j]
                elif i-j == 0:
                    ans += mat[i][j]
        return ans