# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    s = []
    if root:
        s += in_traversal(root.left)
        s.append(root.val)
        s += in_traversal(root.right)
    return s


class Solution:
    def bstToGst(self, root):
        s = 0
        if not root:
            return 0
        s += self.bstToGst(root.right)
        s += root.val
        print(s)
        s += self.bstToGst(root.left)
        return s


a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(5)
g = TreeNode(6)
h = TreeNode(7)
i = TreeNode(8)

e.left = b
e.right = g
b.left = a
b.right = c
c.right = d
g.left = f
g.right = h
h.right = i

print(in_traversal(e))
S = Solution()
S.bstToGst(e)
