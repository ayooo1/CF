class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ret = []
        m = max(candies)
        for i in candies:
            if i+extraCandies >= m:
                ret.append(True)
            else:
                ret.append(False)
        
        return ret