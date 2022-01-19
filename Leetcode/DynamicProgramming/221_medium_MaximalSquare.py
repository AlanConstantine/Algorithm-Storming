# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-19 16:25:47

# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

#  

# 示例 1：


# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 示例 2：


# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 示例 3：

# 输入：matrix = [["0"]]
# 输出：0
#  

# 提示：

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maximalSquare(self, matrix) -> int:
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return 0
        max_ = 0
        dp = [[0 for c in range(col)] for r in range(row)]
        if matrix[0][0] == '1':
            dp[0][0] = 1
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1],
                                       dp[r-1][c-1]) + 1  # 取最小,短板效应
                    max_ = max(max_, dp[r][c])
        return max_ * max_


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalSquare(matrix))
