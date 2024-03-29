# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 15:00:26

# 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

# 给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

# 示例 1:

# 输入:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# 输出: True
# 解释:
# 在上述矩阵中, 其对角线为:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
# 各条对角线上的所有元素均相同, 因此答案是True。
# 示例 2:

# 输入:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# 输出: False
# 解释:
# 对角线"[1, 2]"上的元素不同。
# 说明:

#  matrix 是一个包含整数的二维数组。
# matrix 的行数和列数均在 [1, 20]范围内。
# matrix[i][j] 包含的整数在 [0, 99]范围内。
# 进阶:

# 如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？
# 如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1, len(matrix)):
            if matrix[i-1][:-1] != matrix[i][1:]:
                return False
        return True


# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]
matrix = [[1, 2],
          [2, 2]]
s = Solution()
print(s.isToeplitzMatrix(matrix))
