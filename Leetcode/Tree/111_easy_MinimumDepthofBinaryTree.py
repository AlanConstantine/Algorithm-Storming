# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 19:17:25


# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明：叶子节点是指没有子节点的节点。
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = [root]
        depth = 1
        while s:
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                if not n.left and not n.right:
                    return depth
                for each in (n.left, n.right):
                    if each:
                        s.append(each)
            depth += 1
