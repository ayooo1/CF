class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        arr = {}
        ans = [0 for i in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in arr:
                arr[nums[i]][2] += (arr[nums[i]][0] - i) * arr[nums[i]][1] 
                arr[nums[i]][1] += 1
                arr[nums[i]][0] = i
            else:
                arr[nums[i]] = [i,1,0]
            ans[i] = arr[nums[i]][2]

        arr = {}
        for i in range(len(nums)):
            if nums[i] in arr:
                arr[nums[i]][2] += (i - arr[nums[i]][0]) * arr[nums[i]][1] 
                arr[nums[i]][1] += 1
                arr[nums[i]][0] = i
            else:
                arr[nums[i]] = [i,1,0] 

            ans[i] += arr[nums[i]][2]       
        
        return ans