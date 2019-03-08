# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-07 23:13:37
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。

# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

# 示例 1:

# 输入:
#     2
#    / \
#   2   5
#      / \
#     5   7

# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 示例 2:

# 输入:
#     2
#    / \
#   2   2

# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global tmp
        tmp = []

        def midtraverse(root):
            if root == None:
                return
            midtraverse(root.left)
            tmp.append(root.val)
            midtraverse(root.right)
        tmp = list(set(tmp))


# 输入: root = [5,3,6,2,4,null,null,1]
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
print(s.findSecondMinimumValue(n1))
