class TreeNode(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.left = None
        self.right = None


class TreeNodePre(object):
    # 带前指针的二叉树节点
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.pre = None
        self.left = None
        self.right = None


def pre_traversal(node):
    # root, left, right
    res = []
    if node:
        res.append(node.val)
        res = res + pre_traversal(node.left)
        res = res + pre_traversal(node.right)
    return res


def post_traversal(node):
    # left, right, root
    res = []
    if node:
        res = post_traversal(node.left)
        res = res + post_traversal(node.right)
        res.append(node.val)
    return res


def in_traversal(node):
    # left, root, right
    res = []
    if node:
        res = in_traversal(node.left)
        res.append(node.val)
        res = res + in_traversal(node.right)
    return res
