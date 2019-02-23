#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 16:03:32
# @Author  : Alan Lau
# @Email   : rlalan@outlook.com

# 在一个给定的数组nums中，总是存在一个最大元素 。

# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

# 如果是，则返回最大元素的索引，否则返回-1。

# 示例 1:

# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.


# 示例 2:

# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.


# 提示:

# nums 的长度范围在[1, 50].
# 每个 nums[i] 的整数范围在 [0, 99].

class Solution(object):

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_num = -1
        max_index = -1
        second_num = 0
        for i in range(len(nums)):
            if nums[i] > max_num:
                second_num = max_num
                max_num = nums[i]
                max_index = i
            elif nums[i] > second_num:
                second_num = nums[i]
        return max_index if max_num >= second_num * 2 else -1


def main():
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.dominantIndex(nums))

if __name__ == '__main__':
    main()
