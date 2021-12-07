# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-07 15:06:17

# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        self.parent = {}
        self.res = []

        def find_parent(root):  # 找出每个节点的父节点
            if not root:
                return
            if root.left:
                self.parent[root.left] = root
            if root.right:
                self.parent[root.right] = root
            find_parent(root.left)
            find_parent(root.right)

        def dfs(root, pre, depth):
            if not root:
                return None
            if depth == k:
                self.res.append(root.val)
                return
            if root.left != pre:  # 用pre记录被访问过的节点方式重复访问
                dfs(root.left, root, depth+1)  # 迭代左节点
            if root.right != pre:
                dfs(root.right, root, depth+1)  # 迭代右节点
            if root in self.parent and self.parent[root] != pre:
                dfs(self.parent[root], root, depth+1)  # 向上迭代父节点

        find_parent(root)
        dfs(target, None, 0)  # 从target开始递归查找
        return self.res


a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(7)
g = TreeNode(4)
h = TreeNode(0)
i = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
c.left = h
c.right = i


print(Solution().distanceK(a, b, 2))
