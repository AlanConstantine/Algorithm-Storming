# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-08 18:48:31

# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        sub = []
        self.ans = False

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            if root.val in sub:
                self.ans = True
                return
            sub.append(k - root.val)
            dfs(root.right)

        dfs(root)
        return self.ans
