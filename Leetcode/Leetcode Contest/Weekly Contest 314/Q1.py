class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        m,mm = float('inf'), float('-inf')
        prev = 0
        for ids,num in logs:
            if num-prev >= mm:
                if num-prev == mm:
                    m = min(m,ids)
                else:
                    mm = num-prev
                    m = ids
            prev = num
        
        return m