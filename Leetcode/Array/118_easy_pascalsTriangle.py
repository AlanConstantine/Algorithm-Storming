# 给定 numRows, 生成帕斯卡三角形的前 numRows 行。

from pprint import pprint


class Solution1:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            newRow = [1]
            for j in range(len(pascal[i - 1])):
                if j + 1 == len(pascal[i - 1]):
                    newRow.append(1)
                    break
                newRow.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            pascal.append(newRow)
        return pascal


class Solution2:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        even = True
        for i in range(2, numRows):
            newRow = [1]
            newRowLen = (i + 1) // 2
            if numRows % 2 == 1:
                newRowLen += 1
                even = False
            for j in range(newRowLen):
                if j + 1 == newRowLen:
                    break
                newRow.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            if even == True:
                newRow = newRow + newRow[::-1]
            else:
                newRow = newRow[:-1] + newRow[::-1]
            pascal.append(newRow)
        return pascal


numRows = 5
pprint(Solution2().generate(numRows))
