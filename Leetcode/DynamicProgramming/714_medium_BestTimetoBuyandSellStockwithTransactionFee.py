# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-08 13:51:01

# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

# 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

#  

# 示例 1：

# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
# 示例 2：

# 输入：prices = [1,3,7,5,10,3], fee = 3
# 输出：6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def maxProfit(self, prices, fee: int) -> int:
        size = len(prices)
        keep = [0] * size  # 手上持有股票时每天最佳收益
        no = [0] * size  # 手上没有持有股票时每天最佳收益
        keep[0] = -1 * prices[0]
        for i in range(1, size):
            # 当天手上持有股票：1:前一天就持有，当天不操作；2:前一天没有，当天买入。对比两种情况的最佳收益（买入股票不收手续费）
            keep[i] = max(keep[i-1], no[i-1]-prices[i])
            # 当天手上没有持有股票：1:前一天本来就没有持有，当天不操作；2:前一天持有，当天卖出并扣除手续费。对比两种情况
            no[i] = max(no[i-1], keep[i-1]+prices[i]-fee)
        return no[-1]  # 手上没有持有股票的收益肯定比持有的多


class Solution:
    # 优化空间
    def maxProfit(self, prices, fee: int) -> int:
        dp = [0, -prices[0]]
        for i in range(1, len(prices)):
            currkeep = max(dp[1], dp[0]-prices[i])
            currno = max(dp[0], dp[1]+prices[i]-fee)
            dp[0], dp[1] = currno, currkeep
        return dp[0]


prices = [1, 3, 7, 5, 10, 3]
fee = 3
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit(prices, fee))
