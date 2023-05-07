class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        n = len(set(nums))
        ret = []
        for i,x in enumerate(nums):
            ret.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        
        return ret