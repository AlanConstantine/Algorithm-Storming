from Tree import TreeNode, pre_traversal


def is_symmetrical(root1, root2):
    # 同为None则对称
    if root1 == None and root2 == None:
        return True
    # 当其中有且只有一个为None的时候则说明不对称，
    # 介于或（or）中当root1与root2同为None时在上一步已作判断
    if root1 == None or root2 == None:
        return False
    # 当同不为None的时候，判断两值是否相等
    if root1.val == root2.val:
        return True
    # 进入递归，判断前序遍历以及对称前序遍历的返回值是否相等
    return is_symmetrical(root1.left, root2.right) and is_symmetrical(root1.right, root2.left)


a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(6)
d = TreeNode(5)
e = TreeNode(5)
f = TreeNode(7)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = f
c.left = g
c.right = e

print(pre_traversal(a))
print(is_symmetrical(a, a))
