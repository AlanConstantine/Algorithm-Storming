# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-16 21:29:55

# 给定一个二叉树，确定它是否是一个完全二叉树。

# 百度百科中对完全二叉树的定义如下：

# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 对于一个合法的完全二叉树，None结点应该是在层序遍历的时候最后被访问到的，
# 如果出现层序遍历访问到None之后依旧还有结点存在，则说明其不满足完全二叉树的要求


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return None
        if root and not root.left and not root.right:
            return True

        s = [root]
        reachnone = False  # 用reachnone标记是否有访问到None
        while s:
            n = s.pop(0)
            if not n:
                reachnone = True  # 碰到了None结点，reachnone标记为True
            else:
                if reachnone:  # 如果reachnone被标记为True且又访问到了不为None的结点，则说明其不满足完全二叉树的定义，返回False
                    return False
                s.append(n.left)
                s.append(n.right)
        return True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = None
c.right = e
c.left = f

print(Solution().isCompleteTree(a))
