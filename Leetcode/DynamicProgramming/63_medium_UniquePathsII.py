# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-18 13:46:04

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


# 网格中的障碍物和空位置分别用 1 和 0 来表示。

#  

# 示例 1：


# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 示例 2：


# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = obstacleGrid.copy()
        if dp[0][0] == 1:
            return 0
        if dp[-1][-1] == 1:
            return 0
        else:
            dp[0][0] = 1
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    continue
                if dp[r][c] == 1:
                    dp[r][c] = 0
                elif r == 0:
                    dp[r][c] = dp[r][c-1]
                elif c == 0:
                    dp[r][c] = dp[r-1][c]
                else:
                    # 要考虑r和c为0时c-1和r-1的边界问题
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]


obstacleGrid = [[0, 1], [0, 0]]
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]

print(Solution().uniquePathsWithObstacles(obstacleGrid))
