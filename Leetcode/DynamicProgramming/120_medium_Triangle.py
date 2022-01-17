# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-17 16:27:34

# 给定一个三角形 triangle ，找出自顶向下的最小路径和。

# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

#  

# 示例 1：

# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 示例 2：

# 输入：triangle = [[-10]]
# 输出：-10

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minimumTotal(self, triangle) -> int:
        size = len(triangle)
        # dp = [[0 for j in range(len(triangle[i]))] for i in range(size)]
        # dp[0] = triangle[0]
        dp = triangle.copy()
        for i in range(1, size):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + \
                        min(dp[i-1][j], dp[i-1][j-1])
        return min(dp[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))
