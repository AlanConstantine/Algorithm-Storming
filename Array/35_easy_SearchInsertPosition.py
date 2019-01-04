# 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
# 你可以假设在数组中无重复元素。


class Solution1:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pointer = 0
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i


class Solution2:
    """二分法查找"""

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left


nums = [1, 3, 5, 6]
target = 5
print(Solution1().searchInsert(nums, target))
