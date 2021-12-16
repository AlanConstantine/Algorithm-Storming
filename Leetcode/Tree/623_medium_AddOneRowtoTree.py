# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-16 21:04:48

# 给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。

# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。

# 将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。

# 如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。

# 示例 1:

# 输入:
# 二叉树如下所示:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5

# v = 1

# d = 2

# 输出:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5

# 示例 2:

# 输入:
# 二叉树如下所示:
#       4
#      /
#     2
#    / \
#   3   1

# v = 1

# d = 3

# 输出:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-one-row-to-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if not root and depth == 1:
            return TreeNode(val)
        if not root and depth != 1:
            return None
        if root and not root.left and not root.right and depth != 1:
            return None
        if depth == 1:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot

        s = [root]
        d = 1  # 栈里存了第一层结点
        while s:
            d += 1  # 取结点，d表示需要被操作的结点层，即当前层+1
            size = len(s)
            if d == depth:  # 到达depth-1层时
                for _ in range(size):
                    n = s.pop(0)  # 取结点
                    l = n.left  # 保存左子树，无所谓是否为None
                    r = n.right  # 保存右子树
                    n.left = TreeNode(val)  # 新建结点
                    n.right = TreeNode(val)  # 新建结点
                    n.left.left = l  # 根据要求拼接原来的左子树
                    n.right.right = r  # 根据要求拼接原来的右子树
                return root
            for _ in range(size):
                n = s.pop(0)
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
d = TreeNode(3)
e = TreeNode(1)
f = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
