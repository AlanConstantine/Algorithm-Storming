# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-07 15:34:07

# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

#  

# 示例 1:

# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:

# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:

# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # 贪心
    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
    def maxProfit(self, prices) -> int:
        res = 0
        size = len(prices)
        for i in range(1, size):
            res += max(0, prices[i]-prices[i-1])
        return res


class Solution2:
    # 动态规划
    def maxProfit(self, prices) -> int:
        size = len(prices)
        dp = [[0, 0] for i in range(size)]
        # dp[i][0]表示表示第i天交易完后手里没有股票的最大利润
        # dp[i][1]表示表示第i天交易完后手里有股票的最大利润
        dp[0][0] = 0
        dp[0][1] = -1*prices[0]  # 第0天持有（即花了price[0]的钱买入）
        for i in range(1, size):
            # 第i天手里没有股票有两种可能：1:前一天也没有持有即dp[i-1][0]，2：或者前一天持有，但是第i天的时候卖出了则利润为dp[i-1][1]+prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 第i天手里持有股票也有两种可能：1:前一天没有持有股票但是今天买入了，2：或者前一天本身就持有股票
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return dp[-1][0]  # 不持有股票状态所得金钱一定比持有股票状态得到的多


class Solution:
    # dp空间优化
    def maxProfit(self, prices) -> int:
        dp = [0, -prices[0]]
        for p in prices:
            dp[0], dp[1] = max(dp[0], dp[1]+p), max(dp[1], dp[0]-p)
        return dp[0]


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))
