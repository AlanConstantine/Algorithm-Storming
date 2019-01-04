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
        last = [1]
        if rowIndex == 0:
            return last
        for i in range(1, rowIndex+1):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(last[j]+last[j-1])
            temp.append(1)
            last = temp
        return last


rowIndex = 5
pprint(Solution().getRow(rowIndex))
