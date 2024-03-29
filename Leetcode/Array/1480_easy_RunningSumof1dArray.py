# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-17 17:15:22

# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

# 请返回 nums 的动态和。

#  

# 示例 1：

# 输入：nums = [1,2,3,4]
# 输出：[1,3,6,10]
# 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
# 示例 2：

# 输入：nums = [1,1,1,1,1]
# 输出：[1,2,3,4,5]
# 解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
# 示例 3：

# 输入：nums = [3,1,2,10,1]
# 输出：[3,4,6,16,17]
#  

# 提示：

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/running-sum-of-1d-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def runningSum(self, nums):
        size = len(nums)
        presum = [0 for i in range(size)]
        presum[0] = nums[0]
        for i in range(1, size):
            presum[i] = nums[i] + presum[i-1]
        return presum


class Solution2:
    # 本地计算,优化空间
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums


class Solution:
    # 本地计算,优化空间
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
