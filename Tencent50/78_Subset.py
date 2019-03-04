# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-04 09:44:19

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def count(s, num):
            res.append(num)
            for i in range(s, len(nums)):
                count(i+1, num+[nums[i]])
        count(0, [])
        return res


class SolutionII(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            nres = res.copy()
            for j in nres:
                res.append([i]+j)
        return res


nums = [1, 2, 3, 4]
s = Solution()
print(s.subsets(nums))
