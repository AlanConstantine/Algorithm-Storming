# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。
# 可以按 任意顺序 返回答案。

class TreeNode(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        self.series = list(range(n))
        self.answer = []
        for i in range(n):
            root = self.getTree(i)
            self.answer.append(root)

    def getTree(self, root_val):
        if root_val == 0:
            pass
        leftseries = self.series[:root_val]
