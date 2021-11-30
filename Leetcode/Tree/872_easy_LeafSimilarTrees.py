# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-30 14:15:45


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False

        def dfs(root, ans):
            if root:
                if not root.left and not root.right:
                    ans.append(root.val)
                    return ans
                ans = dfs(root.left, ans)
                ans = dfs(root.right, ans)
            return ans

        return dfs(root1, []) == dfs(root2, [])


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c

e = TreeNode(1)
f = TreeNode(2)
g = TreeNode(3)

e.left = f
e.right = g

print(Solution().leafSimilar(a, e))
