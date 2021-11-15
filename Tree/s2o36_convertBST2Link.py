from Tree import TreeNode, in_traversal

# [4, 6, 8, 10, 12, 14, 16]


def convertBST2Linked(root):
    # 中序遍历
    if not root:
        return None

    convertBST2Linked(root.left)
    c.relink(root)
    convertBST2Linked(root.right)


class Conveter():
    def __init__(self):
        self.head = None

    def relink(self, root):
        if not self.head:
            root.left = self.head
            self.head = root
        else:
            self.head.right = root
            root.left = self.head
            self.head = root

    def gethead(self):
        return self.head


def printhead(root):
    if not root:
        return None
    if root.right:
        rightval = root.right.val
    else:
        rightval = 'None'
    if root.left:
        leftval = root.left.val
    else:
        leftval = 'None'
    print(root.val, '--right-->', rightval)
    print(root.val, '--left--->', leftval)

    printhead(root.left)


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
c = Conveter()
convertBST2Linked(a)
head = c.gethead()
printhead(head)
