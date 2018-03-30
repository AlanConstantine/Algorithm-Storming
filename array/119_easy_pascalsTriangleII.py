# 给定一个索引 k，返回帕斯卡三角形（杨辉三角）的第 k 行。
# 例如，给定 k = 3，
# 则返回 [1, 3, 3, 1]。
from pprint import pprint


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]
        pascal = [1, 1]
        even = True
        for i in range(2, rowIndex):
            newRow = [1]
            newRowLen = (i + 1) // 2
            if rowIndex % 2 == 1:
                newRowLen += 1
                even = False
            for j in range(newRowLen):
                if j + 1 == newRowLen:
                    break
                newRow.append(pascal[j] + pascal[j + 1])
            if even == True:
                newRow = newRow + newRow[:: -1]
            else:
                newRow = newRow[: -1] + newRow[:: -1]
            pascal = newRow
        return pascal


rowIndex = 5
pprint(Solution().getRow(rowIndex))
