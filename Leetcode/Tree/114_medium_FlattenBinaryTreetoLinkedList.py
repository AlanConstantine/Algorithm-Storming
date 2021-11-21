# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-21 09:17:41

# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(root):
            res = []
            if root:
                res.append(root)
                res += dfs(root.left)
                res += dfs(root.right)
            return res

        s = dfs(root)
        root = s.pop(0)
        while s:
            root.right = s.pop(0)
            root.left = None
            root = root.right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        s = [root]
        pre = TreeNode(0)
        while s:
            cur = s.pop()
            if cur.right:
                s.append(cur.right)  # 因为使用了pop(),先进后出，所以先把right放进栈里
            if cur.left:
                s.append(cur.left)
            pre.right = cur
            pre.left = None
            pre = cur
