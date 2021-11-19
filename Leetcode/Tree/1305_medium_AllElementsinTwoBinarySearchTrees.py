# 给你 root1 和 root2 这两棵二叉搜索树。

# 请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        def dfs(root):
            res = []
            if root:
                res += dfs(root.left)
                res.append(root.val)
                res += dfs(root.right)
            return res

        return sorted(dfs(root1) + dfs(root2))
