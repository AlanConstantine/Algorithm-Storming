#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-22 23:27:14
# @Author  : Alan Lau
# @Email   : rlalan@outlook.com

# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

# 示例 1:

# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  示例 2:

# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 注意：

# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        pass


def main():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    print(s.minCostClimbingStairs(cost))

if __name__ == '__main__':
    main()
