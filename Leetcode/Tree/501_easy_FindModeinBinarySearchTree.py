# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-17 14:39:29

# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

# 假定 BST 有如下定义：

# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST [1,null,2,2],

#    1
#     \
#      2
#     /
#    2
# 返回[2].

# 提示：如果众数超过1个，不需考虑输出顺序

# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 双指针在递增序列中找出众数，可能会有多个众数


class Solution:
    def findMode(self, root: TreeNode):
        if not root:
            return

        results = []
        max_count = 0
        count = 0
        base = None

        def dfs(root):
            nonlocal max_count, count, base, results
            if not root:
                return
            dfs(root.left)
            if base != root.val:
                base = root.val
                count = 1
            else:
                count += 1
            if count == max_count:
                results.append(root.val)
            if count > max_count:
                max_count = count
                results = []
                results.append(root.val)

            dfs(root.right)

        dfs(root)
        return results


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(3)

a.right = b
b.left = c
b.right = d
d.left = e
e.left = f

print(Solution().findMode(a))
