# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-16 15:54:24

# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

# 子数组 是数组中的一个连续序列。

#  

# 示例 1：

# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
# 示例 2：

# 输入：nums = [1]
# 输出：0


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/arithmetic-slices
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    # 动态规划
    def numberOfArithmeticSlices(self, nums) -> int:
        size = len(nums)
        if size < 3:
            return 0
        dp = [0] * size
        if nums[2] - nums[1] == nums[1] - nums[0]:
            dp[2] = 1
        diff = nums[2] - nums[1]  # 记录前两位公差
        for i in range(3, size):
            if nums[i] - nums[i-1] == diff:
                dp[i] = dp[i-1]+1  # 如果满足公差相同,则方案累加并+1,具体可以自己举例子验证
            else:
                diff = nums[i] - nums[i-1]  # 否则重置公差
                dp[i] = 0  # 当前i保持0方案
        return sum(dp)


nums = [1, 2, 3, 4, 5]
print(Solution().numberOfArithmeticSlices(nums))
