# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。

# 其中，克隆树 cloned 是原始树 original 的一个 副本 。

# 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。


# 思路：同时遍历两个树，因为clone的，所以结构完全相同，只需要判断target符合original中的节点，那么同时访问到的cloned节点就是目标值
class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original:
            if original is target:
                return cloned
            res = self.getTargetCopy(original.left, cloned.left, target)
            if res:  # 如果res非空，说明找到目标节点，则无需执行右节点的遍历，直接返回
                return res
            res = self.getTargetCopy(original.right, cloned.right, target)
            if res:
                return res

        return None
