# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 15:39:47


# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：

# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# https://leetcode-cn.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        if abs(ldepth-rdepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0
            leftd = dfs(root.left)
            rightd = dfs(root.right)
            if leftd == -1:  # 利用-1作为标记
                return -1
            if rightd == -1:
                return -1
            # 如果
            # 如果绝对值大于1就返回-1，否则返回自己的深度
            return -1 if abs(leftd-rightd) > 1 else max(leftd, rightd) + 1
        return False if dfs(root) == -1 else True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
a.left = b
a.right = c
d = TreeNode(3)
e = TreeNode(3)
b.left = d
b.right = e
f = TreeNode(4)
g = TreeNode(4)
d.left = f
d.right = g

print(Solution().isBalanced(a))
