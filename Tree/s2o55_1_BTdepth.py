from Tree import TreeNode, pre_traversal


class Stack():
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def get_length(self):
        return len(self.stack)


def BTmaxdepth1(root):
    maxd = 0
    if not root:
        return maxd

    def get_max_depth(root, maxd):
        if not root:
            return maxd

        if not root.left and not root.right:
            S.push(root)
            len_ = S.get_length()
            if len_ > maxd:
                maxd = len_
            S.pop()
            return maxd
        S.push(root)
        maxd = get_max_depth(root.left, maxd)
        maxd = get_max_depth(root.right, maxd)
        S.pop()
        return maxd

    return get_max_depth(root, maxd)


def BTmaxdepth(root):
    if not root:
        return 0
    leftd = BTmaxdepth(root.left)
    rightd = BTmaxdepth(root.right)
    return leftd+1 if leftd > rightd else rightd+1
    # 利用return的逆方向计算和传递长度


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = g
c.right = f

print(pre_traversal(a))
S = Stack()
# print(BTmaxdepth1(a))
print(BTmaxdepth(a))
