# Question: 
# 217. Contains Duplicate :
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
        return False
