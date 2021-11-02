# Definition for a binary tree node.
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
        pass


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

S = Solution()

a = S.buildTree(preorder, inorder)
print(in_traversal(a))
print(pre_traversal(a))
