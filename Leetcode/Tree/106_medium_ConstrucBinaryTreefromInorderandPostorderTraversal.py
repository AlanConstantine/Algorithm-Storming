# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-22 13:51:58

# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None
        self.check = {v: i for i, v in enumerate(inorder)}  # 利用哈希表存储中序遍历节点的位置

        def iter(lefti, endi):
            # lefti， righti分别为后序遍历中的下标
            if lefti > endi:
                return None
            rootval = postorder.pop()  # 因为是后序遍历，所以最后一个元素一定是根节点，取出来作根节点
            root = TreeNode(rootval)
            mid = self.check[rootval]
            # 因为是后序遍历，所以右子树节点分布在后序遍历的右侧，从后面取出根节点，所以从右子树开始递归
            root.right = iter(mid+1, endi)
            root.left = iter(lefti, mid-1)  # 右子树递归结束后，后序遍历里才只会剩下左子树的节点
            return root
        return iter(0, len(postorder)-1)
