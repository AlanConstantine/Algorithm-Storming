# https://leetcode-cn.com/problems/NYBBNL/
# 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，
# 使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def help(root):
            q = []
            if root:
                q += help(root.left)
                q.append(root)
                q += help(root.right)
            return q

        q = help(root)

        newtree = q.pop(0)
        newroot = newtree
        newroot.left = None

        while q:
            newtree.right = q.pop(0)
            newtree.left = None
            newtree = newtree.right
        return newroot
