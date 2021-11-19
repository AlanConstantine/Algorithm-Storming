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
    p = TreeNode(-1)  # 要学会定义一个辅助节点呀！！！

    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = self.p

        def inorder(root):
            if root:
                inorder(root.left)
                self.p.right = root  # 中序遍历到最左节点，把左节点连接到锚节点上
                root.left = None  # 当前节点的左节点肯定为空，因为上一层递归有if root，判断后返回值就是None
                # 而对于中间其他节点的左节点来说，因为左节点比中间节点和右节点优先访问到，所以先一步组装到了新的树上
                # 因此可以大胆的设置root.left = None
                self.p = root
                inorder(root.right)
            return None
        inorder(root)
        return res.right
