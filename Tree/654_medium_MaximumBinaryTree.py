# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-07 22:50:17

# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。

# Example 1:

# 输入: [3,2,1,6,0,5]
# 输入: 返回下面这棵树的根节点：

#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# 注意:

# 给定的数组的大小在 [1, 1000] 之间。

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionII(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def maxIndex(nums, start, end):
            max_index = start
            for i in range(start, end+1):
                if nums[i] > nums[max_index]:
                    max_index = i
            return max_index

        def buildtree(nums, start, end):
            if start > end:
                return None
            max_index = maxIndex(nums, start, end)
            n = TreeNode(nums[max_index])
            n.left = buildtree(nums, start, max_index-1)
            n.right = buildtree(nums, max_index+1, end)
            return n

        return buildtree(nums, 0, len(nums)-1)


nums = [3, 2, 1, 6, 0, 5]
s = Solution()
root = s.constructMaximumBinaryTree(nums)
print(root.val)
print(root.left.val)
