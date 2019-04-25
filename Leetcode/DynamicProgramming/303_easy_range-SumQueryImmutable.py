# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-04-26 02:23:30

# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

# 示例：

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:

# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < j:
            self.nums[i] = self.nums[i]+self.sumRange(i, j-1)
        print(self.nums)
        return self.nums[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(2, 5))
