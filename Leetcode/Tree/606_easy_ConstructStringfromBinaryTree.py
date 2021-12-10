# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-10 11:55:48

# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

# 示例 1:

# 输入: 二叉树: [1, 2, 3, 4]
#        1
#      /   \
#     2     3
#    /
#   4

# 输出: "1(2(4))(3)"

# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
# 示例 2:

# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4

# 输出: "1(2()(4))(3)"

# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def tree2str(self, root) -> str:
        if not root:
            return ''

        def dfs(root):
            if not root:
                return ''
            head = str(root.val)
            L = dfs(root.left)
            R = dfs(root.right)
            if len(L) == 0 and len(R) == 0:
                return head
            if len(L) == 0 and len(R) != 0:
                return '{}({})({})'.format(head, L, R)
            if len(L) != 0 and len(R) == 0:
                return '{}({})'.format(head, L)
            return '{}({})({})'.format(head, L, R)
        return dfs(root)


class Solution:
    def tree2str(self, root) -> str:
        if not root:
            return ''

        def dfs(root):
            if not root:
                return ''
            head = str(root.val)
            if not root.left and not root.right:
                return head
            if not root.left and root.right:
                return '{}()({})'.format(head, dfs(root.right))
            if root.left and not root.right:
                return '{}({})'.format(head, dfs(root.left))
            return '{}({})({})'.format(head, dfs(root.left), dfs(root.right))
        return dfs(root)
# 示例1：
# 输入: root = [1,3,2,5,3,null,9]
# 解释:
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9


# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(5)
# e = TreeNode(3)
# f = TreeNode(9)

# a.left = c
# a.right = b
# b.right = f
# c.left = d
# c.right = e

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
b.right = d
print(Solution().tree2str(a))
