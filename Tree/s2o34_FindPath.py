from Tree import TreeNode, pre_traversal
from uitls import Stack


def find_path(root, targ):
    if not root:
        return None

    if root.val > targ:
        return None

    if root.val == targ:
        S.push(root)
        S.show()

    if root.val < targ:
        S.push(root)
        targ = targ - root.val


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(4)
e = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e

print(pre_traversal(a))
S = Stack()
