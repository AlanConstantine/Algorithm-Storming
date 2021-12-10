# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-10 15:26:03

# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

# 编码的字符串应尽可能紧凑。

#  

# 示例 1：

# 输入：root = [2,1,3]
# 输出：[2,1,3]
# 示例 2：

# 输入：root = []
# 输出：[]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root:
                res.append('None')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')

        def help(res):
            if len(res) == 0:
                return None
            val = res.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = help(res)
            root.right = help(res)
            return root
        return help(res)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
