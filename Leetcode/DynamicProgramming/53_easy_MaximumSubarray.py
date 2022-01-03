# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-03 14:27:01

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组 是数组中的一个连续部分。

#  

# 示例 1：

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：

# 输入：nums = [1]
# 输出：1
# 示例 3：

# 输入：nums = [5,4,-1,7,8]
# 输出：23

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # 动态规划
    def maxSubArray(self, nums) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0] * size  # 用dp存储每一个下标之前的最大连续子数组的和
        dp[0] = nums[0]  # 第一个下标最大连续数组和就是下标0自己的值
        # 第二个： 考虑是否和上一个下标进行连续还是不连续，对比两种情况的结果
        # 每一个下标有两种状态：
        # 和上一个下标进行连续，则结果为dp[i-1]+nums[i]
        # 不和上一个下标进行连续，新起一个连续数组,则结果为nums[i]
        # 对比两种状态的结果
        dp[1] = max(nums[1], dp[0]+nums[1])
        for i in range(2, size):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


class Solution2:
    # 动态规划2
    def maxSubArray(self, nums) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0] * size  # 用dp存储每一个下标之前的最大连续子数组的和
        dp[0] = nums[0]  # 第一个下标最大连续数组和就是下标0自己的值
        # 第二个： 考虑是否和上一个下标进行连续还是不连续，对比两种情况的结果
        # 每一个下标有两种状态：
        # 和上一个下标进行连续，则结果为dp[i-1]+nums[i]
        # 不和上一个下标进行连续，新起一个连续数组,则结果为nums[i]
        # 对比两种状态的结果
        # dp[1] = max(nums[1], dp[0]+nums[1])
        for i in range(1, size):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


class Solution:
    def maxSubArray(self, nums) -> int:
        pass


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
