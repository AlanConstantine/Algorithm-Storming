# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-24 18:11:45

# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

# 示例 1:

# 输入: [3, 2, 1]

# 输出: 1

# 解释: 第三大的数是 1.
# 示例 2:

# 输入: [1, 2]

# 输出: 2

# 解释: 第三大的数不存在, 所以返回最大的数 2 .
# 示例 3:

# 输入: [2, 2, 3, 1]

# 输出: 1

# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。

import math


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = -1*math.inf
        second = -1 * math.inf
        third = -1 * math.inf
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num < first and num > second:
                third = second
                second = num
            elif num < second and num > third:
                third = num
        return third if third != -1 * math.inf else first


nums = [2, 2, 3, 1]
S = Solution()
print(S.thirdMax(nums))
