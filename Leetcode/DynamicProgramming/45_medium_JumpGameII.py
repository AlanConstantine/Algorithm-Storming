# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-02 17:41:11

# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。

#  

# 示例 1:

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:

# 输入: nums = [2,3,0,1,4]
# 输出: 2

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # 动态规划，超出时间限制
    def jump(self, nums) -> int:
        size = len(nums)
        if size == 1:
            return 0
        dp = [float("inf")] * size
        dp[0] = 0
        for i in range(size):
            for j in range(i):
                max_index = j + nums[j]  # 检查当前元素之前的所有能到达的最大位置
                if max_index >= i:  # 只有最大位置大于当前下标的时候才进行比较
                    dp[i] = min(dp[i], dp[j]+1)  # 依次对比取最小值
        return dp[-1]


class Solution:
    # 贪心
    # 找出每个下标最大能访问的范围内最大值
    def jump(self, nums) -> int:
        size = len(nums)
        maxpos = 0
        end = 0  # 边界，如果下标i触及跳跃的边界，则跳跃次数+1
        step = 0
        for i in range(size-1):
            # if maxpos >= i:
            maxpos = max(maxpos, i+nums[i])
            if i == end:  # 遇到边界，就更新边界，并且步数加一
                end = maxpos  # 用最大的访问范围更新边界，在最大范围内的i都不需要更新下标
                step += 1
        return step


nums = [1, 2, 1, 1, 1]
print(Solution().jump(nums))
