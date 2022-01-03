# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-02 16:32:32

# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。

#  

# 示例 1：

# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：

# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#  

# 提示：

# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] <= 105

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 非动态规划解法
class Solution1:
    def canJump(self, nums) -> bool:
        size = len(nums)
        if size == 0:
            return False
        # 用0和1表示是否能被访问
        dp = [0] * size  # 所有阶梯初始状态设为0
        if size == 1:  # nums=[0]为特例
            return True
        if nums[0] > 0:  # 否则当nums的长度不为1且nums[0]的值为0时，第一个阶梯访问不到后面的所有阶梯，则返回false，否则dp[0]设为1表示能被访问
            dp[0] = 1
        else:
            return False
        # 满足要求的条件是dp所有阶梯都能被访问，即sum(dp) == len(dp)
        for i in range(size):
            if dp[i] == 0:  # 判断当前的阶梯是否被访问过，如果没有被访问过则表示无法到达此阶梯，返回False
                return False
            steps = nums[i]
            if i+steps >= size-1:
                return True
            if steps == 0:
                continue
            if sum(dp[i:i+steps+1]) == len(dp[i:i+steps+1]):
                continue
            for j in range(i, i+steps+1):
                dp[j] = 1  # 将可访问的范围设为1
        return sum(dp) == size


class Solution:
    # 贪心算法
    # 基本思路：遍历数组更新记录最大可以到达的下标即可，然后判断最大可达的下标是否大于等于数组长度
    def canJump(self, nums) -> bool:
        max_i = 0  # 定义最大能跳到的下标
        for i, jump in enumerate(nums):
            # 如果max_i大于等于当前下标i，说明当前i能被访问到。且如果当前位置+跳数>最远位置，则更新最大能到达的位置下标， 否则小于max_i没必要更新
            if max_i >= i and i + jump > max_i:
                max_i = i + jump
        return max_i >= len(nums)-1


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
