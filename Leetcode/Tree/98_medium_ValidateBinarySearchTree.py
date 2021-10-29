# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-10-29 11:45:55

# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    s = []
    if root:
        s += in_traversal(root.left)
        s.append(root.val)
        s += in_traversal(root.right)
    return s


class Solution:
    def __init__(self) -> None:
        self.last = -1*math.inf

    def isValidBST(self, root):
        if not root:
            return True
        if self.isValidBST(root.left):
            if root.val > self.last:
                self.last = root.val
                return self.isValidBST(root.right)
        return False


a = TreeNode(1)
b = TreeNode(1)
# c = TreeNode(3)

a.left = b
# a.right = c

# print(in_traversal(a))
S = Solution()
print(S.isValidBST(a))
