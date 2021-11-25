# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-25 13:10:55

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:  # 当root为空或者等于p或者等于q的时候， 返回root
            return root
        leftb = self.lowestCommonAncestor(root.left, p, q)  # 在左子树查是否存在p和q
        rightb = self.lowestCommonAncestor(root.right, p, q)  # 在左子树查是否存在p和q
        if not leftb:  # 如果左子树没有则说明p和q在右子树上
            return rightb
        if not rightb:  # 如果右子树没有则说明在左子树上
            return leftb
        if leftb and rightb:  # 如果左右子树存在，说明当前节点为目标节点
            return root
        return None  # 否则返回空， 即左右子树都不存在p和q
