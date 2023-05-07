import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        ans = []
        best = []

        for x in obstacles:
            idx = bisect.bisect_right(best,x)

            if idx >= len(best):
                best.append(x)
            else:
                best[idx] = x

            
            ans.append(idx+1)
        
        return ans