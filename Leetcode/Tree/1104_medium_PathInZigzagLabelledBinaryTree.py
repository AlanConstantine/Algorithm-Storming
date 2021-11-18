# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。


# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

import math


class Solution:
    def pathInZigZagTree(self, label: int):
        row = int(math.log2(label))+1  # 根据数学规律利用label定位行数
        ans = [0]*row  # 一行一个父节点，所以ans有row维
        while row:
            ans[row-1] = label  # 将当前label加入到ans中
            label = (2**row-1-label+2**(row-1))//2  # 找出label的父节点
            row -= 1  # 行号-1

        return ans


print(Solution().pathInZigZagTree(26))
