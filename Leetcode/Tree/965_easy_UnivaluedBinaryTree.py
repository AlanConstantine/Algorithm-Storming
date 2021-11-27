# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-27 17:05:28


# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
# https://leetcode-cn.com/problems/univalued-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    num_ = set()

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.num_.add(root.val)
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right) and len(self.num_) == 1


class Solution:

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.num_ = set()

        def dfs(root):
            if not root:
                return
            self.num_.add(root.val)
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return len(self.num_) == 1


a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(1)
d = TreeNode(1)

a.right = b
b.left = c
b.right = d
a = TreeNode(0)
print(Solution().isUnivalTree(a))
