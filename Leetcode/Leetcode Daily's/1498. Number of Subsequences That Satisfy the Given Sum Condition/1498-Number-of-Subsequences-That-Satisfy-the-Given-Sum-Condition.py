class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9+7
        ans = 0
        nums.sort()

        l=0
        r=len(nums)-1

        while l <= r:
            while l <= r and nums[l]+nums[r] > target:
                r -= 1
            
            if l > r:
                break
            
            ans += pow(2,(r-l),mod)
            ans %= mod
            l += 1



        return ans%mod