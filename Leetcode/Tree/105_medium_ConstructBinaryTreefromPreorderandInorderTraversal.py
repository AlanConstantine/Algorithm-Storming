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
        res += in_traversal(root.left)
        res += in_traversal(root.right)
    return res


class Solution:
    def buildTree(self, preorder, inorder):
        self.index_ = {preorder[i]: i for i in range(len(preorder))}

    def generate(self, ls, le, rs, re, preorder, inorder):
        # ls: left start index
        # le: left end index
        # rs: rigth start index
        # re: right end index
        root = TreeNode(preorder[0])
        root_index = self.index_[preorder[0]]
        le = root_index
        rs = root_index + 1
        left_inorder = inorder[ls: le]
        right_inorder = inorder[rs: re]

        left_


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

S = Solution()

a = S.buildTree(preorder, inorder)
print(in_traversal(a))
print(pre_traversal(a))
