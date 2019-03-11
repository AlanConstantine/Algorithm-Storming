# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-09 21:19:40

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 注意p,q必然存在树内, 且所有节点的值唯一!!!
# 递归思想, 对以root为根的(子)树进行查找p和q, 如果root == null || p || q 直接返回root
# 表示对于当前树的查找已经完毕, 否则对左右子树进行查找, 根据左右子树的返回值判断:
# 1. 左右子树的返回值都不为null, 由于值唯一左右子树的返回值就是p和q, 此时root为LCA
# 2. 如果左右子树返回值只有一个不为null, 说明只有p和q存在与左或右子树中, 最先找到的那个节点为LCA
# 3. 左右子树返回值均为null, p和q均不在树中, 返回null


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归思想, 对以root为根的(子)树进行查找p和q, 如果root == null || p || q 直接返回root
        if root == None or root == p or root == q:
            return root
        # 表示对于当前树的查找已经完毕, 否则对左右子树进行查找, 根据左右子树的返回值判断:
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left == None and right == None:
            # 1. 左右子树返回值均为null, p和q均不在树中, 返回null
            return None
        elif left != None and right != None:
            # 2. 左右子树的返回值都不为null, 由于值唯一左右子树的返回值就是p和q, 此时root为LCA
            return root
        else:
            # 3. 如果左右子树返回值只有一个不为null, 说明只有p和q存在与左或右子树中, 最先找到的那个节点为LCA
            return right if left == None else left


n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n8
n5.right = n9
n3.left = n6
n3.right = n7

s = Solution()
print(s.lowestCommonAncestor(n1).val)
