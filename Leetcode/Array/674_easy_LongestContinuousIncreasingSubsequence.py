# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-02-23 16:30:45

# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。

# 示例 1:

# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
# 示例 2:

# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        con_num = 1
        long_num = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                con_num += 1
                if con_num > long_num:
                    long_num = con_num
            else:
                con_num = 1
        return long_num


def main():
    nums = [1, 3, 5, 4, 7]
    s = Solution()
    print(s.findLengthOfLCIS(nums))


if __name__ == "__main__":
    main()
