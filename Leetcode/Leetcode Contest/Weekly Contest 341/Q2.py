class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        ans = -1
        ret = 0
        for i in divisors:
            m = 0
            for x in nums:
                if x%i == 0:
                    m += 1
            if ans < m:
                ans = m
                ret = i
            elif ans == m:
                ret = min(i,ret)
        return ret