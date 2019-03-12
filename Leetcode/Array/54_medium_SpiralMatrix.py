# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-05 16:35:47

# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:

# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:

# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        m = len(matrix)
        n = len(matrix[0])
        step = m*n
        right = 0
        down = n-1
        left = m-1
        up = 0
        while step > 0:
            # right
            for r in range(up, down+1):
                if step == 0:
                    return res
                res.append(matrix[right][r])
                step -= 1
            right += 1

            # down
            for d in range(right, left+1):
                if step == 0:
                    return res
                res.append(matrix[d][down])
                step -= 1
            down -= 1

            # left
            for l in range(down, up-1, -1):
                if step == 0:
                    return res
                res.append(matrix[left][l])
                step -= 1
            left -= 1

            # up
            for u in range(left, right-1, -1):
                if step == 0:
                    return res
                res.append(matrix[u][up])
                step -= 1
            up += 1
        return res


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
# matrix = [[1, 2, 3, 4, 5],
#           [16, 17, 18, 19, 6],
#           [15, 24, 25, 20, 7],
#           [14, 23, 22, 21, 8],
#           [13, 12, 11, 10, 9]]
s = Solution()
print(s.spiralOrder(matrix))
