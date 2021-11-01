# Definition for a binary tree node.
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    res = []
    if root:
        res += in_traversal(root.left)
        res.append(root.val)
        res += in_traversal(root.right)
    return res


class Solution1:
    def levelOrder(self, root):
        if not root:
            return []
        self.res = []
        self.getchild(root, 0)
        return self.res

    def getchild(self, root, depth):
        if not root:
            return
        if len(self.res) <= depth:
            self.res.append([])

        self.res[depth].append(root.val)
        self.getchild(root.left, depth+1)
        self.getchild(root.right, depth+1)


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        stack = [root]  # 利用stack储存被访问节点的下一层节点
        while stack:
            tmp = []
            stack_tmp = []
            for node in stack:  # 取同一层的节点出来
                tmp.append(node.val)
                if node.left:
                    stack_tmp.append(node.left)  # 将同一层节点的左节点存入
                if node.right:
                    stack_tmp.append(node.right)  # 将同一层节点的右节点存入
            res.append(tmp)
            stack = stack_tmp
        return res


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
a.left = b
a.right = c

d = TreeNode(15)
e = TreeNode(7)

c.left = d
c.right = e
print(in_traversal(a))
S = Solution()
print(S.levelOrder(a))
