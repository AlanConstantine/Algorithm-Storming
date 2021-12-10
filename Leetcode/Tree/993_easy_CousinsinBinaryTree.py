# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-10 16:06:03

# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        s = [root]
        while s:
            level = []
            size = len(s)
            for _ in range(size):
                n = s.pop(0)
                child = []
                if n.left:
                    s.append(n.left)
                    child.append(n.left.val)
                    level.append(n.left.val)
                if n.right:
                    s.append(n.right)
                    child.append(n.right.val)
                    level.append(n.right.val)
                if x in child and y in child:
                    return False
            if x in level and y in level:
                return True
        return False
