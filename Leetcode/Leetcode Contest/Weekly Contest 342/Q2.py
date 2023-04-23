class Solution:
    def sumOfMultiples(self, n: int) -> int:
        lst = []
        for x in range(3,n+1):
            if x%3 == 0 or x%5==0 or x%7==0:
                lst.append(x)
        return sum(lst)