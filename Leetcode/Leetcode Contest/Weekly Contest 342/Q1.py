class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        ans = arrivalTime + delayedTime
        return ans%24