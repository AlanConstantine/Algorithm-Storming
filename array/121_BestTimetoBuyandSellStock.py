# 假设你有一个数组，其中第 i 个元素是一支给定股票第 i 天的价格。

# 如果您只能完成最多一笔交易（即买入和卖出一股股票），则设计一个算法来找到最大的利润。


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minpoint = prices[0]
        maxpoint = prices[0]
        tempmin = prices[0]
        tempmax = prices[0]
        maxprofit = maxpoint - minpoint
        for i in range(len(prices)):
            if i + 1 == len(prices):
                break
            if prices[i + 1] < tempmin:
                tempmin = prices[i + 1]
                tempmax = prices[i + 1]
                continue
            if prices[i + 1] > tempmax:
                tempmax = prices[i + 1]
            else:
                tempmax = prices[i]
            if tempmax - tempmin > maxprofit:
                maxpoint = tempmax
                minpoint = tempmin
            maxprofit = maxpoint - minpoint
        return maxprofit


class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit, mini = 0, prices[0]
        for i in prices:
            if i > mini:
                profit = max(profit, i - mini)
            else:
                mini = i
        return profit


prices = [2, 4, 1]
prices2 = [3, 2, 6, 5, 0, 3]
print(Solution2().maxProfit(prices2))
