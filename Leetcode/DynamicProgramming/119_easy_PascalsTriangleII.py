# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-16 17:11:01

# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。


#  

# 示例 1:

# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:

# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:

# 输入: rowIndex = 1
# 输出: [1,1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def getRow(self, rowIndex: int):
        res = [[1]]
        if rowIndex == 0:
            return res[0]
        for i in range(1, rowIndex+1):
            row = [1 for e in range(i+1)]
            for j in range(1, i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        # print(res)
        return res[-1]


rowIndex = 3
print(Solution().getRow(rowIndex))
