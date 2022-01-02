# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-07 13:38:48


# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

#  

# 示例 1：

# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：

# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 向后考虑打劫
class Solution1:

    def rob(self, nums) -> int:
        if not nums:
            return 0
        # 用数组存储是否打劫每个房子的最优结果，超出两个的原因是要考虑最后一个房子的最优解
        self.res = [0] * (len(nums) + 2)

        def help(h):
            if h == len(nums)-1:
                self.res[h] = nums[h]  # 如果是最后一个房子，则最优收益就是偷当前的房子
                return
            # 每个房子有两种状态，不被偷和被偷，用max取最大值
            res = max(nums[h] + self.res[h+2], self.res[h+1])
            self.res[h] = res  # 然后将结果存入数组中
            return
        h = len(nums) - 1
        while h >= 0:  # 从后向前遍历，获取每个房子的最优解，这样遍历当每个房子时候，就可以获取当前房子的下一个或者下下一个房子的最优解
            help(h)
            h -= 1

        return max(self.res)

# 向前考虑打劫


class Solution2:

    def rob(self, nums) -> int:
        if not nums:
            return nums
        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size  # dp为记录最优解的数组
        dp[0] = nums[0]  # 第一个房子的最优解是自己，因为向前考虑的话前面没有房子
        dp[1] = max(nums[1], dp[0])  # 第二个房子的最优解是考虑自己和前一个房子取最优解
        for h in range(2, size):
            # 后续的房子只需要考虑自己+前前房子的最优解或者前一个房子的最优解
            dp[h] = max(dp[h-2]+nums[h], dp[h-1])
        return dp[-1]


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        dp = [0] * n  # 构建存储数组，存储打劫第i个房子的最有解
        dp[0] = nums[0]  # 第一个房子的最优解就是自己
        dp[1] = max(nums[0], nums[1])  # 第二个房子就是看前一个房子和当前房子的最优解
        for i in range(2, n):
            # 如果打劫上一个房子，那当前房子就不打劫，则+0，如果打劫前前一个房子，则可以打劫当前房子所以要加上当前房子的收益
            dp[i] = max(dp[i-1]+0, dp[i-2]+nums[i])
        return dp[-1]  # 打劫完后返回最后一个房子的解


nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
        168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
print(Solution().rob(nums))
