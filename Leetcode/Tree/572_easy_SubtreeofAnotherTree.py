# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-26 13:30:10

# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subtree-of-another-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            return root.val == subroot.val and dfs(root.left, subroot.left) and dfs(root.right, subroot.right)
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return '#'
            # root = [12] 和 subRoot = [2], 要在 val 值两边加符号 " 来区分 2 不是 12 的有效子树，即高亮树的根节点
            return '"{}"-{}-{}'.format(root.val, dfs(root.left), dfs(root.right))
        return dfs(subRoot) in dfs(root)


a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)

f = TreeNode(4)
g = TreeNode(1)
h = TreeNode(2)
i = TreeNode(3)

# exp1
a.left = b
a.right = c
b.left = d
b.right = e

f.left = g
f.right = h

# exp2
# a = TreeNode(1)
# b = TreeNode(1)

# c = TreeNode(1)

# a.left = b

# exp3
# a.left = b
# a.right = c
# b.left = d
# c.left = e

# i.left = g
# i.right = h

# exp4
# a = TreeNode(12)
# f = TreeNode(2)

print(Solution().isSubtree(a, f))
