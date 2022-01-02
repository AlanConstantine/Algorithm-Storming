# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-02 12:33:28

# 给你一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

#  

# 示例 1：

# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 示例 2：

# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#  

# 提示：

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-and-earn
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def deleteAndEarn(self, nums) -> int:
        maxv = max(nums)
        earns = [0] * (maxv+1)
        for i in nums:
            earns[i] += 1
        # 按照nums的值构造earns数组，earns数组的下标表示nums中的earn，下标对应的值则为earn出现的次数
        # 在earns上构建动态规划：
        # 如果考虑下标i，则不能考虑相邻的下标。即i-1和i+1，则问题就和打家劫舍相似
        # 且下标i的收益为earns[i]*i，因为earns[i]表示在i在nums中出现次数，i表示nums中的收益
        size = len(earns)
        dp = [0] * size
        dp[0] = earns[0]
        dp[1] = max(earns[0], earns[1]*1)
        for i in range(2, size):
            dp[i] = max(dp[i-1]+0, dp[i-2]+earns[i]*i)
        return dp[-1]


a = [2, 2, 3, 3, 3, 4]
print(Solution().deleteAndEarn(a))
