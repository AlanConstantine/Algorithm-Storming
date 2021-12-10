# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-10 13:26:28

# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

# 两棵树重复是指它们具有相同的结构以及相同的结点值。

# 示例 1：

#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# 下面是两个重复的子树：

#       2
#      /
#     4
# 和

#     4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        counter = {}
        ans = []
        if not root:
            return ans

        def dfs(root):
            ans_ = ''
            if not root:
                return ''
            head = str(root.val)
            if root.left and root.right:
                ans_ = '{}({})({})'.format(
                    head, dfs(root.left), dfs(root.right))
            if root.left and not root.right:
                ans_ = '{}({})'.format(head, dfs(root.left))
            if not root.left and root.right:
                ans_ = '{}()({})'.format(head, dfs(root.right))
            if not root.left and not root.right:
                ans_ = head
            if ans_ in counter and counter[ans_]:
                ans.append(root)
                counter[ans_] = False
            if ans_ not in counter:
                counter[ans_] = True
            return ans_
        dfs(root)
        return ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(4)
g = TreeNode(4)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
e.left = g

Solution().findDuplicateSubtrees(a)
