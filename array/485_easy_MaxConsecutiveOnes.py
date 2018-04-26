# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-04-26 22:03:23

# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:

# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：

# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                if temp > counter:
                    counter = temp
                    temp = 0
                else:
                    temp = 0
        if temp > counter:
            counter = temp
            temp = 0
        return counter


class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
                if temp >= counter:
                    counter = temp
            else:
                temp = 0
        return counter


nums = [1, 1, 0, 1, 1, 1]
num = Solution2().findMaxConsecutiveOnes(nums)
print(num)
