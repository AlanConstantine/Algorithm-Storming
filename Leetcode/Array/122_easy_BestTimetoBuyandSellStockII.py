# 假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

# 设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。

# 示例 1:

# 输入: prices = [7, 1, 5, 3, 6, 4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#           随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:

# 输入: prices = [1, 2, 3, 4, 5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#           注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:

# 输入: prices = [7, 6, 4, 3, 1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        tprofit, profit, mini = 0, 0, prices[0]
        for i in range(len(prices)):
            if prices[i] > mini:
                tprofit = prices[i] - mini
                profit += tprofit
                mini = prices[i]
            else:
                mini = prices[i]
        return profit

# 其实这道题很简单，把选择买入卖出的点可以看成
# 由于股票的购买没有限制，因此整个问题等价于寻找 x个不相交的区间 (l_i,r_i]使得如下的等式最大化
# 继续等价于区间为1的价值和，所以仅需要考虑每个间隔为一的区间的价值是否大于0，若大于0，
# 则将该区间的价值加起来即可


class Solution:
    def maxProfit(self, prices) -> int:
        res = 0  # 保存价值
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])  # 若区间产生的价值大于0，则加入到res中
        return res


prices = [1, 2, 4]
prices2 = [3, 2, 6, 5, 0, 3]
print(Solution().maxProfit(prices2))
