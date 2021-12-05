# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-05 14:11:35

# 你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。

# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = 1e6
        self.pre = -1

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre == -1:
                self.pre = root.val
            else:
                self.ans = min(self.ans, root.val-self.pre)
                self.pre = root.val
            dfs(root.right)

        dfs(root)
        return self.ans
