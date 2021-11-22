# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-22 13:20:40

# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）

# 题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 因为是BST，所以首先一定知道前序遍历的第一个节点就是根节点，
    # 而且我们可以知道值大于根节点的一定在右子树，小于根节点的一定在左子树
    # 所以取到根节点的值后，利用递归构造出BST即可
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder.pop(0))

        rootval = preorder.pop(0)
        root = TreeNode(rootval)
        leftpre = [i for i in preorder if i <= rootval]
        rightpre = preorder[len(leftpre):]
        root.left = self.bstFromPreorder(leftpre)
        root.right = self.bstFromPreorder(rightpre)
        return root
