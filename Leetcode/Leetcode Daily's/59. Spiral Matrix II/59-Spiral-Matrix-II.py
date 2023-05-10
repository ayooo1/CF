class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0 for i in range(n)] for j in range(n)]

        t,l = 0, 0
        r,b = n, n
        c = 1
        while l<r and t<b:
            for i in range(l,r):
                res[t][i]=c
                c+=1


            t += 1

            for j in range(t,b):
                res[j][r-1]=c
                c+=1


            r -= 1

            if not (l<r and t<b):
                break

            for i in range(r-1,l-1,-1):
                res[b-1][i]=c
                c+=1


            b -= 1

            for j in range(b-1,t-1,-1):
                res[j][l]=c
                c+=1


            l += 1

        return res