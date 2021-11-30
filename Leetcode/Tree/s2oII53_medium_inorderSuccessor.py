# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-30 16:43:48

# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。

# 节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/P5rCT8
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None

        self.f = False
        self.ans = None

        def dfs(root):
            if root:
                dfs(root.left)
                if self.f and not self.ans:
                    self.ans = root
                    # self.f = False
                    return
                if root is p:
                    self.f = True
                dfs(root.right)
            return
        dfs(root)
        return self.ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
e = TreeNode(4)
f = TreeNode(5)
g = TreeNode(6)
f.left = c
f.right = g

c.left = b
c.right = e
b.left = a

print(Solution().inorderSuccessor(f, a).val)
