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
        pass

    def generaten(self, i):
        if i == 1:
            leaf = TreeNode(1)
            return
        if i == 2:
            leaf2 = TreeNode(2)
            pass
        while i > 1:
            pass
