# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-05 13:30:04


# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return
        self.ans = 1e6
        self.pre = -1

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre == -1:
                self.pre = cur.val
            else:
                self.ans = min(self.ans, cur.val - self.pre)
                self.pre = cur.val
            dfs(cur.right)

        dfs(root)
        return self.ans


a = TreeNode(236)
b = TreeNode(104)
c = TreeNode(701)
d = TreeNode(227)
e = TreeNode(911)

a.left = b
a.right = c
b.right = d
c.right = e

print(Solution().getMinimumDifference(a))
