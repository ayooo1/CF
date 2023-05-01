from sortedcontainers import SortedList
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        sl = SortedList(range(len(nums)))
        arr = sorted([[nums[i]] + [i] for i in range(len(nums))])
        n = len(arr)
        res, prev = 0, 0
        for i, (_, idx) in enumerate(arr):
            if prev <= sl.index(idx):
                res+=sl.index(idx)-prev
            else:
                res+=sl.index(idx)+(n-prev)
            n-=1
            prev = sl.index(idx)
            res+=1
            sl.remove(idx)
        return res