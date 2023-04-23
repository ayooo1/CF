class Solution:
    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a%b)
        
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones: return n - ones
        ans = float("inf")
        
        for l in range(n):
            g = nums[l]
            for r in range(l+1, n):
                g = self.gcd(g, nums[r])
                if g == 1:
                    ans = min(ans, r-l + (n-1))
                    break
        
        return ans if ans != float("inf") else -1