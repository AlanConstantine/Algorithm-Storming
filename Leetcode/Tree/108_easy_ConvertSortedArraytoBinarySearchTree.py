# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_traversal(root):
    a = []
    if root:
        a += in_traversal(root.left)
        a.append(root.val)
        a += in_traversal(root.right)
    return a

# 思路：关键词是二叉搜索树，且要求等高。那每次生成节点的时候从数组中间开始提取即可


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        if len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        if len(nums) > 2:
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            leftnums = nums[:mid]
            rightnums = nums[mid+1:]
            root.left = self.sortedArrayToBST(leftnums)
            root.right = self.sortedArrayToBST(rightnums)
            return root


nums = [-10, -3, 0, 5, 9]
S = Solution()
print(in_traversal(S.sortedArrayToBST(nums)))
