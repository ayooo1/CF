class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = []
        right = [0 for _ in range(n)]
        left.append(nums[0])
        #prefix
        for i in range(1, n):
            left.append(left[i - 1] | nums[i])
        
        #suffix
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] | nums[i]
        
        #calculation
        result = 0
        for i in range(n):
            result = max(result, (nums[i] << k | (0 if i == 0 else left[i - 1]) | (0 if i == n - 1 else right[i + 1])))
        
        return result