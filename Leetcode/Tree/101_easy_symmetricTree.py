# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    if not root:
        return []
    a = []
    a += in_traversal(root.left)
    a.append(root.val)
    a += in_traversal(root.right)
    return a


class Solution:
    def isSymmetric(self, root):
        return self.compare(root, root)

    def compare(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.compare(a.left, b.right) & self.compare(a.right, b.left)
        else:
            return False


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
d = None
e = TreeNode(4)
f = TreeNode(3)
g = TreeNode(2)

a.left = b
a.right = g
b.left = c
b.right = d
g.left = e
g.right = f


print(in_traversal(a))
S = Solution()
print(S.isSymmetric(a))
