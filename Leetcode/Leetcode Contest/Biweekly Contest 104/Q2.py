from heapq import heappop,heappush


class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        ans = 0
        lst = []
        for _ in range(len(nums[0])):
            for i in range(len(nums)):
                m =max(nums[i])
                heappush(lst,(-m,(i,nums[i].index(m))))
            m = heappop(lst)
            ans += -m[0]
            nums[m[1][0]][m[1][1]] = 0
            while lst:
                _, (x,y) = heappop(lst)
                nums[x][y] = 0
                
                
        return ans