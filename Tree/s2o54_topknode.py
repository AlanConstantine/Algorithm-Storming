from Tree import TreeNode, in_traversal


def searchtopKBST(root, k):

    def in_tra(root):
        s = []
        if not root:
            return []

        s += in_tra(root.left)
        s.append(root)
        s += in_tra(root.right)
        return s

    s = in_tra(root)
    return s[::-1][k-1]


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(7)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(6)
g = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(in_traversal(a))
print(searchtopKBST(a, k=2).val)
