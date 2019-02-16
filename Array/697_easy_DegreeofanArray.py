#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-16 10:31:35
# @Author  : Alan Lau
# @Email   : rlalan@outlook.com

# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

# 示例 1:

# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
# 示例 2:

# 输入: [1,2,2,3,1,4,2]
# 输出: 6


class Solution:

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = [0, i, i]
            d[v][0] += 1
            if i <= d[v][1]:
                d[v][1] = i
            if i >= d[v][2]:
                d[v][2] = i
        res = sorted(d.items(), key=lambda x: (
            x[1][0], x[1][1] - x[1][2]), reverse=True)[0]
        return res[1][2] - res[1][1] + 1


def main():
    s = Solution()
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(s.findShortestSubArray(nums))

if __name__ == '__main__':
    main()
