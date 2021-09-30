from Tree import TreeNode, post_traversal


def verityBST(postlist):
    if len(postlist) <= 0:
        return False
    if len(postlist) == 1:
        return True
    if len(postlist) == 2:
        if postlist[0] < postlist[1]:
            return True
        else:
            return False

    root = postlist[-1]

    i = 0
    while i < len(postlist)-1:
        if postlist[i] > root:
            break

    if i == 0:
        return False

    lefttree = postlist[:i]
    righttree = postlist[i:-1]
    return verityBST(lefttree) and verityBST(righttree)


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

postlist = post_traversal(a)

print(verityBST(postlist))
