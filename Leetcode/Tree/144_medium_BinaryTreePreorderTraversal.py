# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-08 15:13:39

# 给定一个二叉树，返回它的 前序 遍历。

#  示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,2,3]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tmp = []

        def pret(root, tmp):
            if not root:
                return
            tmp.append(root.val)
            pret(root.left, tmp)
            pret(root.right, tmp)
        pret(root, tmp)
        return tmp
