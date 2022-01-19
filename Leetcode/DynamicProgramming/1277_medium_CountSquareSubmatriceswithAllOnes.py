# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-19 18:52:45

# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

#  

# 示例 1：

# 输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释：
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
# 示例 2：

# 输入：matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#  

# 提示：

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def countSquares(self, matrix) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = 0

        dp = [[0 for c in range(col)]
              for r in range(row)]  # 下标为[i][j]为右下角的正方形的数目为
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = matrix[r][c]
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1],
                                       dp[r-1][c-1]) + 1
                else:
                    dp[r][c] = 0
                ans += dp[r][c]
        return ans


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

print(Solution().countSquares(matrix))
