# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-08 15:06:35

# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global tmp
        tmp = []

        def midt(root):
            if not root:
                return
            midt(root.left)
            tmp.append(root.val)
            midt(root.right)
        midt(root)
        return tmp


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
print(s.inorderTraversal(n1))
