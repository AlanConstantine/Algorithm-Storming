# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-08 19:05:05

# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

# 行数 m 应当等于给定二叉树的高度。
# 列数 n 应当总是奇数。
# 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
# 每个未使用的空间应包含一个空的字符串""。
# 使用相同的规则输出子树。
# 示例 1:

# 输入:
#      1
#     /
#    2
# 输出:
# [["", "1", ""],
#  ["2", "", ""]]
# 示例 2:

# 输入:
#      1
#     / \
#    2   3
#     \
#      4
# 输出:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/print-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: TreeNode):
        if not root:
            return None

        def getdepth(root):
            if not root:
                return 0
            return max(getdepth(root.left), getdepth(root.right)) + 1

        depth = getdepth(root)
        res = [['' for w in range((2**depth-1))] for d in range(depth)]

        def fill(root, l, r, i):
            if not root:
                return
            res[i][(l+r)//2] = str(root.val)
            fill(root.left, l, (l+r)//2, i+1)
            fill(root.right, (l+r)//2+1, r, i+1)

        fill(root, 0, len(res[0]), 0)
        return res


# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
e = TreeNode(2)
f = TreeNode(1)
g = TreeNode(3)
h = TreeNode(4)
i = TreeNode(7)
e.left = f
e.right = g
f.right = h
g.right = i

pprint(Solution().printTree(e))
