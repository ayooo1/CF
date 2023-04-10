import math
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        m = float('-inf')
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i == j:
                    m = max(m, nums[i][j] if is_prime(nums[i][j]) else 0)
                elif i + j == len(nums)-1:
                    m = max(m, nums[i][j] if is_prime(nums[i][j]) else 0)

        return m