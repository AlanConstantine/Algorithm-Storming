# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-24 22:25:40

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_nums = sorted(nums)
        return sum(s_nums[::2])


nums = [1, 2, 3, 2]
S = Solution()
print(S.arrayPairSum(nums))
