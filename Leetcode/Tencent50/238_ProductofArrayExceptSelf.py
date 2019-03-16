# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-15 19:10:58

# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

# 示例:

# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in range(len(nums))]
        right = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))

# https://blog.csdn.net/qq_17550379/article/details/83854155
# 首先想到的思路就是将所有元素乘起来，然后遍历数组中的元素再除以对应元素即可。但是这种做法很快被驳回，我们不可以使用除法。非常简单，我们可以遍历nums，在遍历的过程中将对应元素累乘，例如
# 1  2  3  4
# 1  1  2  6

# 这样我们就得到了对应元素左边所有元素的乘积。然后我们反向遍历nums，做相同操作即可。
# 1  2  3  4
# 24 12 4  1

# 再将两个结果相乘即可。
# 1  2  3  4
# 24 12 8  6
