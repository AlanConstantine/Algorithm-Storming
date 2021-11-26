# -*- coding: utf-8 -*-
# @Author: LIU Ruilun (laualan@hku.hk)
# @Date: 2021-11-26 13:02:07

# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/h54YBf
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ','.join(self.serizahelp(root))

    def serizahelp(self, root):
        res = []
        if root:
            res.append(str(root))
            res += self.serizahelp(root.left)
            res += self.serizahelp(root.right)
        else:
            res.append('None')
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.deseriahelp(data.split(','))

    def deseriahelp(self, rootlist):
        val = rootlist.pop(0)
        if val == 'None':
            return None
        root = TreeNode(int(val))
        root.left = self.deseriahelp(rootlist)
        root.right = self.deseriahelp(rootlist)
        return root

        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # ans = deser.deserialize(ser.serialize(root))


root = "1,2,3,None,None,4,5"
Codec().deserialize(root)
