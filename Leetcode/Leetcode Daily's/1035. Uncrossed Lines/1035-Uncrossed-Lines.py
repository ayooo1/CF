from functools import cache


class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        @cache
        def dfs(i,j):
            if i == len(nums1) or j ==len(nums2):
                return 0
            ans = 0
            if nums1[i] == nums2[j]:
                ans = 1+dfs(i+1,j+1)
            else:
                ans = max(dfs(i+1,j), dfs(i,j+1))
            
            return ans
        
        return dfs(0,0)