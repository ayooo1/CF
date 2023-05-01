class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        m = max(nums)
        ans = 0
        while k:
            ans += m
            m += 1
            k-=1
        return ans