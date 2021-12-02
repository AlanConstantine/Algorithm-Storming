# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-02 09:34:15

# 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

# 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

# CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/complete-binary-tree-inserter
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        s = [self.root]
        self.d = []  # 用一个节点来维护没有满足完全二叉树要求的节点
        while s:  # 用层序遍历找出缺少根节点的节点
            n = s.pop(0)
            if not n.left or not n.right:  # 找出所有不满足要求的节点并存入二叉树中
                self.d.append(n)
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)

    def insert(self, val: int) -> int:
        newnode = TreeNode(val)  # 构造新节点
        parnode = self.d[0]  # 取出第一个缺少根节点的节点
        self.d.append(newnode)  # 把新节点加入到队列中，因为新节点肯定没有子节点的
        if not parnode.left:  # 如果取出来的节点没有左节点
            parnode.left = newnode
        else:
            parnode.right = newnode  # 如果右节点填满后
            self.d.pop(0)  # 被取出来的节点两个子节点都有了，因此要从队列中取出来
        return parnode.val

    def get_root(self) -> TreeNode:
        return self.root

        # Your CBTInserter object will be instantiated and called as such:
        # obj = CBTInserter(root)
        # param_1 = obj.insert(val)
        # param_2 = obj.get_root()
