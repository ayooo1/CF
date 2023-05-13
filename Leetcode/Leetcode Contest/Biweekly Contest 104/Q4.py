class Solution:
    def sumOfPower(self, nums: list[int]) -> int:
        mod, n = int(1e9+7), len(nums)
        #Sort Nums
        #Take prefix sum
        #Point to current largest
        #For each largest number, square it, multiply it by the sum of numbers at or below it
        #Gives the number of 
        nums.sort()
        pref = nums.copy()
        for i in range(1, n):
            pref[i] += pref[i-1]<<1
        res = 0
        for i in range(n):
            res += (nums[i]**2)*(nums[i]+(pref[i-1] if i > 0 else 0))
            res%=mod
        return res%mod