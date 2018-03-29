# 1.two sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr_dict = {}
        for i in range(len(nums)):
            red = target - nums[i]
            if red in arr_dict:
                return [arr_dict[red], i]
            arr_dict[nums[i]] = i


nums = [3, 2, 4]
target = 6
s = Solution().twoSum(nums, target)
print(s)
