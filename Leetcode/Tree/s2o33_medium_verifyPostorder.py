# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-11 14:14:20

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

#  

# 参考以下这颗二叉搜索树：

#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：

# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：

# 输入: [1,3,2,6,5]
# 输出: true

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def verifyPostorder(self, postorder) -> bool:

        def help(postorder, start, end):
            if start >= end:
                return True
            p = start
            while postorder[p] < postorder[end]:  # 用p获取左子树
                p += 1
            mid = p
            while postorder[p] > postorder[end] and p != end:  # 用p获取右子树
                p += 1

            if p < end:  # 当不满足BST的后序时，p在遍历右子树时肯定会提前结束，造成p<end，即不满足BST后序的条件
                return False
            return help(postorder, start, mid-1) and help(postorder, mid, end-1)

        return help(postorder, 0, len(postorder)-1)


# pos = [1, 2, 5, 10, 6, 9, 4, 3]
pos = [1, 3, 2, 6, 5]
print(Solution().verifyPostorder(pos))
