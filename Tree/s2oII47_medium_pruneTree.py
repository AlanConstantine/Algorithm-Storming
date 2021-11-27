# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-27 16:15:36

# 给定一个二叉树 根节点 root ，树的每个节点的值要么是 0，要么是 1。请剪除该二叉树中所有节点的值为 0 的子树。

# 节点 node 的子树为 node 本身，以及所有 node 的后代。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pOCWxh
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:  # 判断当前节点的值以及子节点的返回值
            return None
        else:
            return root


a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(0)
d = TreeNode(1)
a.right = b
b.left = c
b.right = d


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


print(inorder(Solution().pruneTree(a)))
