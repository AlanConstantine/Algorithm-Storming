# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 09:42:03

# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        val = preorder[0]
        root = TreeNode(val)
        # 这里的inorder不是原来的inorder，而是被截取过的inorder
        root_index = inorder.index(val)
        root.left = self.buildTree(
            preorder[1: root_index+1], inorder[:root_index])
        # 因此preorder[1: root_index+1]，中的root_index的索引刚好能表示中序遍历中左子树的长度，而中序遍历长度和前序遍历的长度是一致的
        root.right = self.buildTree(
            preorder[root_index+1:], inorder[root_index+1:])
        return root


def inorder_(root):
    res = []
    if root:
        res += inorder_(root.left)
        res.append(root.val)
        res += inorder_(root.right)
    return res


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

print(inorder_(Solution().buildTree(preorder, inorder)))
