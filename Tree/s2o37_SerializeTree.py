from Tree import TreeNode, pre_traversal


def serialize(root):
    series = []
    if not root:
        series.append('$')
        return series
    series.append(root.val)
    series += serialize(root.left)
    series += serialize(root.right)
    return series


def deserialize(series):
    if not series:
        return None, series
    if series[0] == '$':
        return None, series
    else:
        root = TreeNode(series[0])
        series = series[1:]
        root.left, series = deserialize(series)
        if series:
            series = series[1:]
            root.right, series = deserialize(series)
            return root, series
        else:
            return None, series
    # for i in range(1, len(series)):
    #     if series[i] == '$':
    #         if root.val == '$':
    #             root.right = None
    #         else:
    #             pass


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
print(pre_traversal(a))
print(serialize(a))
root, s = deserialize(serialize(a))
print(pre_traversal(root))
