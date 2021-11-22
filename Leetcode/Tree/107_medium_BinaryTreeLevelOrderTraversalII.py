# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-22 11:19:01

# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树[3, 9, 20, null, null, 15, 7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层序遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            ans.append([n.val for n in s])
            stmp = []
            for n in s:
                if n.left:
                    stmp.append(n.left)
                if n.right:
                    stmp.append(n.right)
            s = stmp
        return ans[::-1]
