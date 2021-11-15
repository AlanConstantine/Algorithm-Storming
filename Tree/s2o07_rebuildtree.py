from Tree import TreeNode, in_traversal, pre_traversal, post_traversal


def rebuildtree(preorder, inorder):
    if (not preorder) or (not inorder):
        return None
    if len(preorder) == 2:
        root = TreeNode(preorder[0])
        if preorder[0] == inorder[0]:
            root.right = TreeNode(inorder[1])
            return root
        else:
            root.left = TreeNode(inorder[0])
            return root

    root = TreeNode(preorder[0])

    if len(preorder) == 1:
        return root

    i = 0
    j = 1
    while i <= len(inorder):
        if inorder[i] == root.val:
            break
        i += 1
    if i != 0:
        inorderleft = inorder[:i]
    else:
        inorderleft = None
        preorderleft = None
    if i + 1 < len(inorder):
        inorderright = inorder[i+1:]
    else:
        inorderright = None
        preorderright = None

    while j < len(preorder) and inorderleft:
        if preorder[j] not in inorderleft:
            break
        j += 1
    preorderleft = preorder[1:j]
    preorderright = preorder[j:]

    root.left = rebuildtree(preorderleft, inorderleft)
    root.right = rebuildtree(preorderright, inorderright)
    return root


preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
t = rebuildtree(preorder, inorder)

print(pre_traversal(t))
print(in_traversal(t))
