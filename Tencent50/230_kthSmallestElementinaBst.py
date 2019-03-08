# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-07 22:51:58

# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

# 示例 1:

# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
# 示例 2:

# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        global sortnode
        sortnode = []

        def midtraverse(root):
            if not root:
                return
            midtraverse(root.left)
            sortnode.append(root.val)
            midtraverse(root.right)
        midtraverse(root)
        return list(set(sortnode))[k-1]


# 输入: root = [5,3,6,2,4,null,null,1], k = 3
n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6

s = Solution()
print(s.kthSmallest(n1, k=3))
