# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

#  

# 示例 1：

# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：

# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3

class Solution:
    def numIslands(self, grid):
        # 利用dfs递归查找周边的岛屿
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            # 如果不等于0则将岛屿淹没
            grid[i][j] = "0"
            dfs(grid, i-1, j)  # 上
            dfs(grid, i+1, j)  # 下
            dfs(grid, i, j-1)  # 左
            dfs(grid, i, j+1)  # 右

        if len(grid) == "0":
            return 0

        nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    nums += 1
                    dfs(grid, i, j)
        return nums


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid))
