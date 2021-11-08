# Definition for a binary tree node.


def preorder(root):
    res = []
    if root:
        res.append(root.val)
        res += preorder(root.left)
        res += preorder(root.right)
    return res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    max_level = 0
    sum_ = 0

    def deepestLeavesSum(self, root):
        self.helper(root, 0)
        return self.sum_

    def helper(self, root, level):
        if root:
            if level > self.max_level:
                self.max_level = level
                self.sum_ = root.val
            elif level == self.max_level:  # 当遍历到最大层时，相加val
                self.sum_ += root.val
            self.helper(root.left, level+1)  # 记录遍历了第几层
            self.helper(root.right, level+1)


class Solution:
    # 层次遍历
    def deepestLeavesSum(self, root):
        sum_ = 0
        stack = [root]  # 利用stack存储遍历到的层的所有节点， 当前root给根节点只有一个
        while len(stack) != 0:
            stack_tmp = []
            for n in stack:  # 遍历stack存到的节点，并利用stack_tmp来存储遍历到的节点的子节点
                if n.left:
                    stack_tmp.append(n.left)
                if n.right:
                    stack_tmp.append(n.right)
            if len(stack_tmp) == 0:  # 当stack_tmp为空的时候，说明当前已经访问到了最深一层
                sum_ = sum([n.val for n in stack])
                break
            stack = stack_tmp
        return sum_


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = g
c.left = f
f.left = h

print(preorder(a))
print(Solution().deepestLeavesSum(a))
