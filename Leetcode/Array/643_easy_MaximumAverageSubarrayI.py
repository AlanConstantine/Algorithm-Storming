# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-02-28 01:36:16
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

# 示例 1:

# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_ = sum(nums[0:k])
        sum_ = max_
        for i in range(k, len(nums)):
            sum_ += -nums[i-k]+nums[i]
            max_ = max(sum_, max_)
        return max_/k


k = 4
nums = [1, 12, -5, -6, 50, 3]
s = Solution()
print(s.findMaxAverage(nums, k))
