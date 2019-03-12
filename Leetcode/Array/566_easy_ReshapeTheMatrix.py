# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-25 13:00:47


# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

# 示例 1:

# 输入:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# 输出:
# [[1,2,3,4]]
# 解释:
# 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        cru_r = len(nums)
        cru_c = len(nums[0])
        if (cru_c == c and cru_r == r) or cru_c*cru_r != c*r:
            return nums

        flat_matrix = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                flat_matrix.append(nums[i][j])
        return [flat_matrix[i:i+c] for i in range(0, len(flat_matrix), c)]


nums = [[1, 2, 3, 4]]
r = 2
c = 2

s = Solution()
print(s.matrixReshape(nums, r, c))
