class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        nums = [0] * n
        res = []
        c = 0
        
        for idx, color in queries:
            prev = nums[idx]
            
            for nei in idx - 1, idx + 1:
                if 0 <= nei < n:
                    if prev == nums[nei] and prev != 0:
                        c -= 1
                    if color == nums[nei]:
                        c += 1
            
            nums[idx] = color
            res.append(c)
        
        return res