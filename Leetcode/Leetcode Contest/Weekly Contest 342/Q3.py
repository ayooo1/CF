from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        ret = []
        h = SortedList()
        for i in range(0,len(nums)):
            h.add(nums[i])
            if len(h) == k:
                ret.append(h[x-1] if h[x-1] < 0 else 0)
                h.discard(nums[i-k+1])
        return ret