# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-21 14:22:15

# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 思路，实际就是BST的定位问题，找到了对应的位置，插入即可
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # 若为空，插入
            return TreeNode(val)
        if root.val > val:
            # 如果当前节点值大于目标值，则说明目标值应该插入当前值的左子树上
            root.left = self.insertIntoBST(root.left, val)
        else:
            # 如果当前节点值小于目标值，则说明目标值应该插入当前值的右子树上
            root.right = self.insertIntoBST(root.right, val)
        return root


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(7)

a.left = b
a.right = e
b.left = c
b.right = d

print(inorder(a))
print(inorder(Solution().insertIntoBST(a, 6)))
