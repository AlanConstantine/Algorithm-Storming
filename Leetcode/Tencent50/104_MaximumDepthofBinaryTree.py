# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-06 16:48:09

# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0

#         depth = 0
#         maxdepth = 0

#         def caln(root, depth, maxdepth):
#             if not root:
#                 return maxdepth
#             caln(root.right)
#             caln(root.left)
#         return caln(root, depth, maxdepth)


class SolutionII(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right))+1


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
print(s.maxDepth(n1))
