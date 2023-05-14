from functools import lru_cache
import math


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(step,mask):
            if mask == (1<<n-1):
                return 0
            
            ans = 0

            for i in range(n):
                if mask & (1<<i) == 0:
                    for j in range(i+1,n):
                        if mask & (1<<j) == 0:
                            ans = max(ans, step * math.gcd(nums[i],nums[j]) + dfs(step+1,mask|(1<<i)|(1<<j)))
            return ans

                

            

            
        return dfs(1,0)