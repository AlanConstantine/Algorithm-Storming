from Tree import TreeNode, in_traversal

# [4, 6, 8, 10, 12, 14, 16]


def convertBST2Linked(root):
    # 中序遍历
    if not root:
        return None
    convertBST2Linked(root.left)
    # do something
    print(root.val)
    convertBST2Linked(root.right)
    pass


a = TreeNode(10)
b = TreeNode(6)
c = TreeNode(4)
d = TreeNode(8)
e = TreeNode(14)
f = TreeNode(12)
g = TreeNode(16)

a.left = b
a.right = e
b.left = c
b.right = d
e.left = f
e.right = g
print(in_traversal(a))
convertBST2Linked(a)
