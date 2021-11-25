# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-25 14:19:22

# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

# 如果有多种构造方法，请你返回任意一种。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balance-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        inorder = self.dfs(root)
        return self.rebuild(inorder)

    def dfs(self, root):
        res = []
        if root:
            res += self.dfs(root.left)
            res.append(root)
            res += self.dfs(root.right)
        return res

    def rebuild(self, inorder):
        if len(inorder) == 0:
            return None
        mid = len(inorder)//2
        root = inorder[mid]
        root.right, root.left = None, None
        root.left = self.rebuild(inorder[:mid])
        root.right = self.rebuild(inorder[mid+1:])
        return root


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.right = b
b.right = c
c.right = d

print(Solution().balanceBST(a))
