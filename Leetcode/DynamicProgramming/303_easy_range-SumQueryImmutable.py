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
        # 在加载数组的时候就对数组进行累加就和，在原数组空间上进行
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j]-self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(2, 5))
