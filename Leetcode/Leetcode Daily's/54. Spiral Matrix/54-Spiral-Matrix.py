class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # set top and left to 0
        t,l = 0, 0
        # set right and bottom to len(matrix[0]) and len(matrix)
        r,b = len(matrix[0]), len(matrix)
        # res = []
        res = []

        # loop should stop if left < right and top < bottom
        while l<r and t<b:
            
            # going left
            for i in range(l,r):
                res.append(matrix[t][i])

            # finished the upper row increment top to go down to the next row
            t += 1

            # finished the left coloumn and decrement right because we want the move the colomn to the left
            for j in range(t,b):
                res.append(matrix[j][r-1])
            
            r -= 1

            # check if this is still not true if its true break
            if not (l<r and t<b):
                break

            # finishing the bottome row and pushing the bottom row up one
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])

            b -= 1

            # finishing the left coloumn and increment the left so the coloumn is closer in the center
            for j in range(b-1,t-1,-1):
                res.append(matrix[j][l])

            l += 1


        return res

