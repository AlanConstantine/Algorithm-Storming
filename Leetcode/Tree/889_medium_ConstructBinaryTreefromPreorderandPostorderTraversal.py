# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-11-28 18:42:24

# 返回与给定的前序和后序遍历匹配的任何二叉树。

#  pre 和 post 遍历中的值是不同的正整数。

#  

# 示例：

# 输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#  

# 提示：

# 1 <= pre.length == post.length <= 30
# pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
# 每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if len(preorder) == 0 or len(postorder) == 0:
            return None
        val = preorder.pop(0)
        postval = postorder.pop()
        root = TreeNode(val)
        if len(postorder) == 0:
            return root
        postlastval = postorder[-1]
        prelastindex = preorder.index(postlastval)

        root.left = self.constructFromPrePost(
            preorder[:prelastindex], postorder[:len(preorder[:prelastindex])])
        root.right = self.constructFromPrePost(
            preorder[prelastindex:], postorder[len(preorder[:prelastindex]):])
        return root


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


print(inorder(Solution().constructFromPrePost(pre, post)))
