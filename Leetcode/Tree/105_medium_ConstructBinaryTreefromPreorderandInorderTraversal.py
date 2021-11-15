# Definition for a binary tree node.
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    res = []
    if root:
        res += in_traversal(root.left)
        res.append(root.val)
        res += in_traversal(root.right)
    return res


def pre_traversal(root):
    res = []
    if root:
        res.append(root.val)
        res += pre_traversal(root.left)
        res += pre_traversal(root.right)
    return res


class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        inorder_root_index = inorder.index(preorder[0])
        root.left = self.buildTree(
            preorder[1: inorder_root_index+1], inorder[: inorder_root_index])
        root.right = self.buildTree(
            preorder[inorder_root_index+1:], inorder[inorder_root_index+1:])
        return root


preorder = [1, 2]
inorder = [2, 1]

S = Solution()

a = S.buildTree(preorder, inorder)
print(in_traversal(a))
print(pre_traversal(a))
