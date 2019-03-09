# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-09 19:58:29

# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tmp = []

        def pos(root, tmp):
            if not root:
                return
            pos(root.left, tmp)
            pos(root.right, tmp)
            tmp.append(root.val)
        pos(root, tmp)
        return tmp
