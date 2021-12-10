# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-09 11:46:47

# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

#  

# 示例 1:

# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:

# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.ans = True

        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            if abs(L-R) > 1:
                self.ans = False
            return max(L, R) + 1
        dfs(root)
        return self.ans


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(1)
f = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = f
d.left = e

print(Solution().isBalanced(a))
