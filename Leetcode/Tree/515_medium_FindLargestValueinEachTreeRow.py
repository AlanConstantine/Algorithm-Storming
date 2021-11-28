# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 19:48:08

# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

#  

# 示例1：

# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
# 解释:
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
# 示例2：

# 输入: root = [1,2,3]
# 输出: [1,3]
# 解释:
#           1
#          / \
#         2   3
# 示例3：

# 输入: root = [1]
# 输出: [1]
# 示例4：

# 输入: root = [1,null,2]
# 输出: [1,2]
# 解释:
#            1
#             \
#              2
# 示例5：

# 输入: root = []
# 输出: []

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        ans = [root.val]

        s = [root]
        while s:
            tmp = []
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                for each in (n.left, n.right):
                    if each:
                        s.append(each)
                        tmp.append(each.val)
            if not tmp:
                break
            ans.append(max(tmp))
        return ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
e = TreeNode(3)
f = TreeNode(9)

a.left = c
a.right = b
b.right = f
c.left = d
c.right = e

print(Solution().largestValues(a))
