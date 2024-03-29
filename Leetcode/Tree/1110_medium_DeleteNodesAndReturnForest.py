# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-03 12:58:06


# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。

# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

# 返回森林中的每棵树。你可以按任意顺序组织答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root:
                return None
            root_del = root.val in to_delete_set  # 用root_del记录当前值是否在目标list中
            if is_root and not root_del:  # 如果父节点是被删除的节点且当前节点不是被删除的节点，则加入到res结果中
                res.append(root)
            root.left = helper(root.left, root_del)
            root.right = helper(root.right, root_del)
            return None if root_del else root  # 如果是目标删除节点，则返回None
        helper(root, True)
        return res


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


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
c.left = f
c.right = g

res = Solution().delNodes(a, [3, 5])

for r in res:
    print(inorder(r))
