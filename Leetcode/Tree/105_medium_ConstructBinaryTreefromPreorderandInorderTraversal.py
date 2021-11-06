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
        self.index_ = {inorder[i]: i for i in range(len(inorder))}

    def generate(self, pres, pree, ins, ine, preorder, inorder):
        # pres: preorder start index
        # pree: preorder end index
        # ins: inorder start index
        # ine: inorder end index
        if pres > pree:
            return None
        root = TreeNode(preorder[pres])
        inorder_root_index = self.index_[preorder[pres]]
        left_tree_size = inorder_root_index - ins
        root.left = self.generate(
            pres+1, pres+left_tree_size, ins, inorder_root_index-1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

S = Solution()

a = S.buildTree(preorder, inorder)
print(in_traversal(a))
print(pre_traversal(a))
