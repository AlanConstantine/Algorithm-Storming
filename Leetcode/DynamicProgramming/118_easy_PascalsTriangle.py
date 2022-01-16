# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-16 16:29:34

# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。


#  

# 示例 1:

# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例 2:

# 输入: numRows = 1
# 输出: [[1]]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[] for i in range(numRows)]
        res[0] = [1]
        res[1] = [1, 1]
        for i in range(2, numRows):
            level = []
            for j in range(len(res[i-1])-1):
                level.append(res[i-1][j]+res[i-1][j+1])
            res[i] = [1] + level + [1]
        return res


class Solution:
    # 空间优化
    def generate(self, numRows: int):
        res = [[1]]
        for i in range(1, numRows):
            row = [1 for e in range(i+1)]
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res


numRows = 6
print(Solution().generate(numRows))
