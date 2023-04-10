class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        if p == 0: return 0
        nums.sort()
        def test(x, p):
            i = 1
            while i < len(nums):
                if nums[i]-nums[i-1] <= x:
                    i+=1
                    p-=1
                    if not p: return 1
                i+=1
            return 0
        
        l, r = -1, nums[-1]-nums[0]
        while r-l>1:
            mid=l+(r-l)//2
            if test(mid, p):
                r = mid
            else:
                l = mid
        return r