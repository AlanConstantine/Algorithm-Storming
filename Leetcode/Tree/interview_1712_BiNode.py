# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-03 10:11:19


# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

# 返回转换后的单向链表的头节点。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binode-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        self.head = TreeNode(-1)
        ans = self.head

        def dfs(root):
            if root:
                dfs(root.left)
                root.left = None
                self.head.right = root
                self.head = root
                dfs(root.right)

        dfs(root)
        return ans.right


a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)

c.left = b
c.right = d
d.right = e
b.left = a


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


print(inorder(c))

print(inorder(Solution().convertBiNode(c)))
