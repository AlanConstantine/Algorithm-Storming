# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-18 14:46:49

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

#  

# 示例 1：


# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：

# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def minPathSum(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = grid.copy()  # dp存储每一个格子的最优结果
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    continue
                # 分别考虑边界
                if r == 0:
                    dp[r][c] += dp[r][c-1]
                elif c == 0:
                    dp[r][c] += dp[r-1][c]
                # 每次取上一步(上一个或者左一个)的结果并加上当前的代价
                else:
                    dp[r][c] += min(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# grid = [[1, 2, 3], [4, 5, 6]]
print(Solution().minPathSum(grid))
