# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-02 13:17:21


# 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧。

# 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

# CBTInserter(TreeNode root) 使用根节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
# CBTInserter.get_root() 将返回树的根节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/NaqhDT
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        s = [root]
        self.d = []
        while s:
            n = s.pop(0)
            if not n.left or not n.right:
                self.d.append(n)
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)

    def insert(self, v: int) -> int:
        par_node = self.d[0]
        self.d.append(TreeNode(v))
        if not par_node.left:
            par_node.left = self.d[-1]
        else:
            par_node.right = self.d[-1]
            self.d.pop(0)
        return par_node.val

    def get_root(self) -> TreeNode:
        return self.root

        # Your CBTInserter object will be instantiated and called as such:
        # obj = CBTInserter(root)
        # param_1 = obj.insert(v)
        # param_2 = obj.get_root()
