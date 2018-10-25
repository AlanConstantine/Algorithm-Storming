# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 14:34:19

# 给定一个矩阵 A， 返回 A 的转置矩阵。

# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。


# 示例 1：

# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
# 示例 2：

# 输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]


# 提示：

# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(A)
        c = len(A[0])
        t_matrix = [[None for i in range(r)] for j in range(c)]
        for i in range(len(A)):
            for j in range(len(A[i])):
                t_matrix[j][i] = A[i][j]
        return t_matrix


class Solution2:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        c = len(A[0])
        flat_matrix = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                flat_matrix.append(A[i][j])
        return [flat_matrix[c_i::c] for c_i in range(c)]


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[1, 2, 3], [4, 5, 6]]
s = Solution()
print(s.transpose(A))
