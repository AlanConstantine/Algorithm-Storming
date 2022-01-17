# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-17 15:33:33

# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

#  

# 示例 1：

# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：下面是两条和最小的下降路径，用加粗+斜体标注：
# [[2,1,3],      [[2,1,3],
#  [6,5,4],       [6,5,4],
#  [7,8,9]]       [7,8,9]]
# 示例 2：

# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：下面是一条和最小的下降路径，用加粗+斜体标注：
# [[-19,57],
#  [-40,-5]]
# 示例 3：

# 输入：matrix = [[-48]]
# 输出：-48
#  

# 提示：

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minFallingPathSum(self, matrix) -> int:
        size = len(matrix)
        dp = [[0 for j in range(size)] for i in range(size)]
        dp[0] = matrix[0]
        for i in range(1, size):
            for j in range(size):
                # 考虑边界,即j为0的时候是不能取到j-1, j为最右边的元素不能取到j+1
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == size-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = matrix[i][j] + \
                        min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
matrix = [[-19, 57], [-40, -5]]
matrix = [[8, 9, 1, 10], [1, 6, 5, 4], [1, 7, 8, 1], [1, 7, 8, 1]]
matrix = [[100, -42, -46, -41], [31, 97, 10, -10],
          [-58, -51, 82, 89], [51, 81, 69, -51]]
print(Solution().minFallingPathSum(matrix))
