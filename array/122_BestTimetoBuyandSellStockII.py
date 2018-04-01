# 假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

# 设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        tprofit, profit, mini, sellpoint = 0, 0, prices[0], prices[0]
        for i in range(len(prices)):
            if prices[i] > mini:
                tprofit = max(prices[i] - mini, tprofit)
                mini = prices[i]
            else:
                mini = prices[i]
                profit += tprofit
                tprofit = 0
        return profit


prices = [2, 4, 1]
prices2 = [3, 2, 6, 5, 0, 3]
print(Solution().maxProfit(prices2))
