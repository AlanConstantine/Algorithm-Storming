# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-20 20:31:05

# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/even-odd-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root) -> bool:
        if not root:
            return False
        if root and not root.left and not root.right and root.val % 2 == 1:
            return True
        if root.val % 2 != 1:
            return False
        s = [root]
        level = []
        depth = 0

        while s:
            stmp = []
            depth += 1
            for node in s:
                if node.left:
                    stmp.append(node.left)
                    if (depth % 2 == 1 and node.left.val % 2 == 1) or (depth % 2 != 1 and node.left.val % 2 != 1):
                        return False
                    level.append(node.left.val)
                if node.right:
                    stmp.append(node.right)
                    if (depth % 2 == 1 and node.right.val % 2 == 1) or (depth % 2 != 1 and node.right.val % 2 != 1):
                        return False
                    level.append(node.right.val)
            if len(stmp) != 0:
                if depth % 2 == 1:  # 奇数层要求偶数且递减
                    for i in range(len(level)-1):
                        if level[i] <= level[i+1]:
                            return False
                else:  # 偶数层要求奇数且递增
                    for i in range(len(level)-1):
                        if level[i] >= level[i+1]:
                            return False
                level = []
            s = stmp
        return True


# a = TreeNode(11)
# b = TreeNode(8)
# c = TreeNode(6)
# a.left = b
# a.right = c

# d = TreeNode(1)
# e = TreeNode(3)
# f = TreeNode(9)
# f1 = TreeNode(11)
# b.left = d
# b.right = e
# c.left = f
# c.right = f1

# g = TreeNode(30)
# h = TreeNode(20)
# i = TreeNode(18)
# j = TreeNode(16)
# l = TreeNode(12)
# m = TreeNode(10)
# n = TreeNode(4)
# o = TreeNode(2)
# p = TreeNode(17)

# d.left = g
# d.right = h
# e.left = i
# e.right = j
# f.left = l
# f.right = m
# f1.left = n
# f1.right = o
# g.left = p

g = TreeNode(11)
h = TreeNode(18)
i = TreeNode(14)
j = TreeNode(3)
l = TreeNode(7)
m = TreeNode(18)
n = TreeNode(6)

g.left = h
g.right = i
h.left = j
h.right = l
l.left = m
m.left = n


print(Solution().isEvenOddTree(g))
