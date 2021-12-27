# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-27 12:12:27


# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

# 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

# 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

# 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

# 示例 1:

# 输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# 输出: true
# 示例 2:

# 输入: "1,#"
# 输出: false
# 示例 3:

# 输入: "9,#,#,1"
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 二叉树也是属于图的结构的一种，因此满足图的条件即：出度总和等于入度总和
# 对于一棵树：
# 非空节点一定有1个入度和2个出度（若子节点为空则连接#也可以表示出度）
# 对于空节点，则只有1个入度没有出度
class Solution1:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':  # 特例
            return True
        preorder = preorder.split(',')
        if len(preorder) == 0:
            return False
        indegree = 0  # 初始化出入度
        outdegree = 0
        for i in range(len(preorder)):
            if i == 0:
                if preorder[i] == '#':  # 当第一个节点为#且preorder长度不为1时，即根节点为空，非法树
                    return False
                outdegree += 2  # 否则根节点的出度为2
                continue
            if preorder[i] == '#':  # 为空节点时，没有出度，只有1个入度
                indegree += 1
            else:  # 否则不为空节点时，入度+1，出度+2
                indegree += 1
                outdegree += 2
            if i != len(preorder) - 1 and indegree >= outdegree:  # 除了最后完成所有遍历，入度应该一直保持小于出度
                return False
        return indegree == outdegree  # 完成遍历后判断入度是否等于出度

# 节点消融
# https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s = []
        for node in preorder.split(','):
            s.append(node)
            while len(s) >= 3 and s[-1] == s[-2] == '#' and s[-3] != '#':
                s.pop(), s.pop(), s.pop()
                s.append('#')
        return len(s) == 1 and s[0] == '#'
