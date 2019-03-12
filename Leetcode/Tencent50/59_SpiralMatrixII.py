# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-05 12:36:34

# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

# 示例:

# 输入: 3
# 输出:
# [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]


from pprint import pprint


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for col in range(n)] for row in range(n)]
        right = 0
        down = n-1
        left = n-1
        up = 0
        c = 0
        while c < n**2:
            # right
            for r in range(up, down+1):
                c += 1
                matrix[right][r] = c
            right += 1
            # down
            for d in range(right, left+1):
                c += 1
                matrix[d][down] = c
            down -= 1
            # left
            for l in range(down, up-1, -1):
                c += 1
                matrix[left][l] = c
            left -= 1
            # up
            for u in range(left, right-1, -1):
                c += 1
                matrix[u][up] = c
            up += 1
        return matrix


n = 4
s = Solution()
pprint(s.generateMatrix(n))
