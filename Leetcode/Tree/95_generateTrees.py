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
        self.answer = []

    def generaten(self, series):
        if not series:
            return None
        for i in range(len(series)):
            newroot = TreeNode(series[i])
            leftseries = series[:i]
            rightseries = series[i+1:]