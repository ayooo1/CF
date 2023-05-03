class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return list((set(nums1) - set(nums2), set(nums2) - set(nums1)))