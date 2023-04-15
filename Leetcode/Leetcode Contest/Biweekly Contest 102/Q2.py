from itertools import accumulate
class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        m, conver = 0, []
        for x in nums:
            m = max(m, x)
            conver.append(x + m)
        return accumulate(conver)