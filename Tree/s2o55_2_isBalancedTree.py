from Tree import TreeNode, pre_traversal


def isbalancedtree(root):
    def balanced(root):
        if not root:
            return 0, True

        leftd, unb = balanced(root.left)
        rightd, unb = balanced(root.right)
        if abs(leftd-rightd) > 1:
            unb = False
        else:
            unb = True
        return leftd+1 if leftd > rightd else rightd+1, unb
    return balanced(root)[1]


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = g
c.right = f
g.left = h
f.right = i

print(pre_traversal(a))
print(isbalancedtree(a))
