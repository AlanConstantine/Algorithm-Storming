# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-29 10:27:31

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a Node.
from _typeshed import SupportsReadline


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 中序遍历访问左节点
            if self.pre:  # 如果前节点存在
                self.pre.right = cur  # 将前节点的右侧连接当前节点
                cur.left = self.pre  # 当前节点的左侧连接前节点，因为中序遍历时当前节点的左子树已经全部遍历完了，所以放心赋值
            else:
                self.head = cur  # 如果不存在前节点，说明是中序遍历结果的最开通头，定位头节点
            self.pre = cur  # 操作结束后将当前节点变成前节点
            dfs(cur.right)  # 中序遍历下一个节点（即有节点）

        self.pre = None
        self.head = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
