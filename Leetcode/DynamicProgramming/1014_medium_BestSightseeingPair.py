# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-07 13:50:22

# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

# 返回一对观光景点能取得的最高分。

#  

# 示例 1：

# 输入：values = [8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# 示例 2：

# 输入：values = [1,2]
# 输出：2
#  

# 提示：

# 2 <= values.length <= 5 * 104
# 1 <= values[i] <= 1000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-sightseeing-pair
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    # 暴力
    def maxScoreSightseeingPair(self, values) -> int:
        size = len(values)
        res = 0
        for i in range(size):
            for j in range(i+1, size):
                res = max(res, values[i] + values[j] + i - j)
        return res


class Solution2:
    def maxScoreSightseeingPair(self, values) -> int:
        size = len(values)
        dp = [0] * size
        dp[0] = values[0] + 0
        res = 0
        for j in range(1, size):
            curr = values[j] - j
            res = max(res, curr+dp[j-1])
            dp[j] = max(values[j]+j, dp[j-1])
        return res


class Solution3:
    # dp优化空间
    # values[i] + values[j] + i - j
    # = values[i] + i + values[j] - j
    # = (values[i] + i) + (values[j] - j)
    # 对于下标j来说，要考虑(values[i] + i) + (values[j] - j)最大值，而因为给定j，(values[j] - j)的值是固定的，所以则求values[i] + i的最大值
    # 而values[i] + i的最大值在遍历values的同时用一个变量premax来维护即可，且有i<j

    def maxScoreSightseeingPair(self, values) -> int:
        premax = values[0] + 0  # 初始第一位premax
        res = 0  # 存储结果
        for j in range(1, len(values)):
            curr = values[j] - j  # 求当前固定值
            res = max(res, premax+curr)  # 维护res结果
            premax = max(premax, values[j]+j)  # 求values[i] + i来维护premax
        return res


class Solution:
    # 第二次dp优化空间
    # values[i] + values[j] + i - j
    # = values[i] + i + values[j] - j
    # = (values[i] + i) + (values[j] - j)
    # 对于下标j来说，要考虑(values[i] + i) + (values[j] - j)最大值，而因为给定j，(values[j] - j)的值是固定的，所以则求values[i] + i的最大值
    # 而values[i] + i的最大值在遍历values的同时用一个变量premax来维护即可，且有i<j

    def maxScoreSightseeingPair(self, values) -> int:
        premax = values[0] + 0  # 初始第一位premax
        res = 0  # 存储结果
        for j in range(1, len(values)):
            res = max(res, premax+values[j] - j)  # 维护res结果
            premax = max(premax, values[j]+j)  # 求values[i] + i来维护premax
        return res


values = [8, 1, 5, 2, 6]
# values = [1, 2]
print(Solution2().maxScoreSightseeingPair(values))
