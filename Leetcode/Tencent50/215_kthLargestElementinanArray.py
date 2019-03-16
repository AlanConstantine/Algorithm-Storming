# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-16 23:40:53

# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort(nums, 0, len(nums)-1)
        return nums[-k]

    def quick_sort(self, nums, left, right):
        if right == left:
            return
        povit = left
        index = left+1
        mid = nums[left]
        for i in range(index, right+1):
            if nums[i] <= mid:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[povit], nums[index-1] = nums[index-1], nums[povit]
        self.quick_sort(nums, left, index-1)
        self.quick_sort(nums, index, right)


class SolutionII(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]


k = 4
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
s = Solution()
print(s.findKthLargest(nums, k))
