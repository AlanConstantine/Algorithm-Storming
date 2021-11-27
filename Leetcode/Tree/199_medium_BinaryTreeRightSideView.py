# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-27 17:32:29

# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# https://leetcode-cn.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []

        s = [root]
        ans = []
        while s:
            ans.append(s[-1].val)
            stmp = []
            for n in s:
                if n.left:
                    stmp.append(n.left)
                if n.right:
                    stmp.append(n.right)
            s = stmp
        return ans
