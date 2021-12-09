# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-12-09 12:22:45

# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3

#  

# 示例 1：

# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：

# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        a = root.left
        b = root.right

        def comp(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val == b.val:
                return comp(a.left, b.right) and comp(a.right, b.left)
            else:
                return False
        return comp(a, b)
