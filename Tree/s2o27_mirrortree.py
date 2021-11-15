from Tree import TreeNode, in_traversal, pre_traversal, post_traversal


def mirror_tree(node):
    if not node:
        return
    if not node.left and not node.right:
        return

    node.left, node.right = node.right, node.left
    if node.left:
        mirror_tree(node.left)
    if node.right:
        mirror_tree(node.right)


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left  # 递归后序遍历，并针对当前节点的左右节点进行交换
        return root


a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(10)
d = TreeNode(5)
e = TreeNode(7)
f = TreeNode(9)
g = TreeNode(11)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(pre_traversal(a))
mirror_tree(a)
print(pre_traversal(a))
