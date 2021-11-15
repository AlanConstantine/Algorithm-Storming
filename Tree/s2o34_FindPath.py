from Tree import TreeNode, pre_traversal


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        elem = self.items.pop()
        return elem

    def get_len(self):
        return len(self.items)

    def get_sum(self):
        sum = 0
        for item in self.items:
            sum += item.val
        return sum

    def show(self):
        show_ = []
        for item in self.items:
            show_.append(item.val)
        print(show_)


def find_path(root):
    if not root:
        # 如果为None，返回
        return

    S.push(root)  # 否则加入栈中准备进行计算sum
    if S.get_sum() == targ:  # 当栈中的总和为目标时
        S.show()  # 打印路径
        S.pop()  # 由于总和已经达到目标值，那么该节点的子节点已经不需要再继续被访问，故将该节点从栈中取出
        return
    elif not root.left and not root.right:  # 如果当前节点的两个子节点都为None，且总和没有满足目标值
        S.pop()  # 则将该节点从栈中取出
        return
    else:  # 否则访问当前节点的子节点，并且在访问结束后从栈中取出
        find_path(root.left)
        find_path(root.right)
        S.pop()  # 被访问结束后的节点需要从栈中取出


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(4)
e = TreeNode(7)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

targ = 22
print(pre_traversal(a))
S = Stack()  # 栈用来存记录走的路径
find_path(a)
