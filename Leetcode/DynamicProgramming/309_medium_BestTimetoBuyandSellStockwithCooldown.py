# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-08 14:17:07

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:

# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        size = len(prices)
        # 三个数组表示不同的状态：当天结束后的最大收益
        keep = [0] * size  # 手上持有股票，说明是前一天就持有的，也可能是前一天没有但当前买入
        no = [0] * size  # 手上没有持有股票但是不处于冷冻期，即说明前一天没有发生交易，也有可能是因为前一天是冷冻期
        # 手上没有持有股票且当天处于冷冻期，即说明当天发生了交易，这里的「处于冷冻期」指的是在第i天结束之后的状态。也就是说：如果第i天结束之后处于冷冻期，那么第i+1天无法买入股票。
        cool = [0] * size
        keep[0] = -prices[0]
        for i in range(1, size):

            keep[i] = max(keep[i-1], no[i-1]-prices[i])
            no[i] = max(no[i-1], cool[i-1])
            # 我们在第i天结束之后处于冷冻期的原因是在当天卖出了股票，那么说明在第i-1天时我们必须持有一支股票，对应的状态为f[i-1][0]加上卖出股票的正收益prices[i]。因此状态转移方程为：
            cool[i] = keep[i-1] + prices[i]

        return max(cool[-1], no[-1])


prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(prices))
