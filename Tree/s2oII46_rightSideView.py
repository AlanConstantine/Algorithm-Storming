# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-21 14:11:20

# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# https://leetcode-cn.com/problems/WNC0Lk/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        res = []
        if not root:
            return res
        res.append(root.val)
        s = [root]
        while s:
            s_tmp = []
            for n in s:
                if n.left:
                    s_tmp.append(n.left)
                if n.right:
                    s_tmp.append(n.right)
            if s_tmp:
                res.append(s_tmp[-1].val)
            s = s_tmp
        return res
