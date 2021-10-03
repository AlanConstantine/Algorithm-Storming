from Tree import TreeNode, in_traversal

# [4, 6, 8, 10, 12, 14, 16]


def convertBST2Linked(root):
    # 中序遍历
    if not root:
        return None

    current_root = root
    if root.left:
        convertBST2Linked(root.left)
    else:
        pass
    # do something
    print(root.val)
    convertBST2Linked(root.right)
    pass


def convet(preroot, nextroot):
    leftnext = nextroot.left
    nextroot.left = preroot
    rightpre = preroot.right
    preroot.right = nextroot
    return leftnext, rightpre


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
