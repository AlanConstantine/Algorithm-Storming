# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-27 16:51:40

# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

# 叶子节点 是指没有子节点的节点。

# https://leetcode-cn.com/problems/binary-tree-paths/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []

        self.ans = []
        self.s = []

        def dfs(root):
            if not root:
                return None
            self.s.append(str(root.val))
            if not root.left and not root.right:
                self.ans.append('->'.join(self.s))
                self.s.pop()
                return
            dfs(root.left)
            dfs(root.right)
            self.s.pop()

        dfs(root)
        return self.ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(3)

a.right = d
a.left = b
b.right = c

print(Solution().binaryTreePaths(a))
