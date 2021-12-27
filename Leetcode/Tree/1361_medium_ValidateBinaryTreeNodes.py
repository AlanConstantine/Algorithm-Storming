# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2021-12-27 13:37:48

# 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

# 只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

# 如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

# 注意：节点没有值，本问题中仅仅使用节点编号。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-tree-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:  # fail
    # 失败的案例
    # n = 4
    # leftChild = [1, 0, 3, -1]
    # rightChild = [-1, -1, -1, -1]
    # 没考虑同时出现环图和两颗树的情况
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        if n == 1 and leftChild[0] != rightChild[0]:
            return False
        degree = {i: [0, 0] for i in range(n)}
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l != -1:
                degree[i][1] += 1
                degree[l][0] += 1
                if degree[l][0] > 1:
                    return False
            if r != -1:
                degree[i][1] += 1
                degree[r][0] += 1
                if degree[r][0] > 1:
                    return False
        indegree = 0
        outdegree = 0
        print(degree)
        root_indegree = False  # 表示是否找到根节点
        for node, degrees in degree.items():
            if degrees[0] == 0 and root_indegree:  # 根节点找到了但是还是存在入度为0的节点，说明出现两颗树
                return False
            if root_indegree and degrees[0] != 1:  # 不为根节点的入度一定为1
                return False  # 如果根节点找到了，但是入度不为1
            if degrees[1] > 2:  # 每个节点的出度不能大于2
                return False
            if degrees[0] == 0 and not root_indegree:  # 根节点入度一定为0， 且根节点的编号不一定为0
                root_indegree = True  # 入度为0且root_indegree为False，说明当前节点为根节点
            indegree += degrees[0]
            outdegree += degrees[1]
        return indegree == outdegree and root_indegree


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        indeg = [0] * n  # 登记入度
        for u in leftChild:
            if u != -1:
                indeg[u] += 1
        for u in rightChild:
            if u != -1:
                indeg[u] += 1

        root = -1
        for i in range(n):
            if indeg[i] == 0:  # 入度为0说明为根节点
                root = i
                break
        if root == -1:  # 入度没有为0的说明为非法树，没有根节点
            return False

        seen = set([root])  # 记录BFS被访问过的节点
        q = [root]

        while len(q) > 0:
            u = q.pop(0)
            if leftChild[u] != -1:
                if leftChild[u] in seen:  # 如果记录中已经被访问过说明为环图，非法树
                    return False
                seen.add(leftChild[u])
                q.append(leftChild[u])
            if rightChild[u] != -1:
                if rightChild[u] in seen:  # 如果记录中已经被访问过说明为环图，非法树
                    return False
                seen.add(rightChild[u])
                q.append(rightChild[u])

        return len(seen) == n


# 作者：LeetCode-Solution
# 链接：https: // leetcode-cn.com/problems/validate-binary-tree-nodes/solution/yan-zheng-er-cha-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


n = 4
leftChild = [1, -1, 3, -1]
rightChild = [2, -1, -1, -1]

# n = 2
# leftChild = [1, 0]
# rightChild = [-1, -1]

# n = 6
# leftChild = [1, -1, -1, 4, -1, -1]
# rightChild = [2, -1, -1, 5, -1, -1]

# leftChild = [3, -1, 1, -1]
# rightChild = [-1, -1, 0, -1]

n = 2
# leftChild = [1, 0]
# rightChild = [-1, -1]
n = 4
leftChild = [1, 0, 3, -1]
rightChild = [-1, -1, -1, -1]
print(Solution().validateBinaryTreeNodes(n, leftChild, rightChild))
