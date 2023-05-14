class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        total = 0 
        for i in derived:
            total = total ^ i

        return total == 0