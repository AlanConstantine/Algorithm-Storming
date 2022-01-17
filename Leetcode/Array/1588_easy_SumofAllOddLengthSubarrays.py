# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-17 17:27:18

# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

# 子数组 定义为原数组中的一个连续子序列。

# 请你返回 arr 中 所有奇数长度子数组的和 。

#  

# 示例 1：

# 输入：arr = [1,4,2,5,3]
# 输出：58
# 解释：所有奇数长度子数组和它们的和为：
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# 示例 2：

# 输入：arr = [1,2]
# 输出：3
# 解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
# 示例 3：

# 输入：arr = [10,11,12]
# 输出：66

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # 前缀和特点: arr[start: end]范围的子数组和为presum[end+1]-presum[start]
    def sumOddLengthSubarrays(self, arr) -> int:
        size = len(arr)
        sum_ = 0
        presum = [0 for i in range(size+1)]
        for i in range(1, size+1):
            presum[i] = arr[i-1] + presum[i-1]
        for start in range(size):
            lenght = 1
            while start+lenght <= size:
                # 动态增加奇数长度的子数组窗口,累加结果
                end = start+lenght-1  # 确定end范围,-1是为了不超过原数组长度
                sum_ += presum[end+1]-presum[start]
                lenght += 2
        return sum_


arr = [1, 4, 2, 5, 3]
print(Solution().sumOddLengthSubarrays(arr))
