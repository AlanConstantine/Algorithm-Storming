# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

# 二叉搜索树保证具有唯一的值。

#  

# 示例 1：

# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32
# 示例 2：

# 输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# 输出：23
#  

# 提示：

# 树中的结点数量最多为 10000 个。
# 最终的答案保证小于 2^31。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/range-sum-of-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preTraversal(root):
    tmp = []

    def pre(root, tmp):
        if not root:
            return
        tmp.append(root.val)
        pre(root.left, tmp)
        pre(root.right, tmp)

    pre(root, tmp)
    return tmp


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        if root.val <= R and root.val >= L:
            sum += root.val
        if root.val >= L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            sum += self.rangeSumBST(root.right, L, R)
        return sum


if __name__ == "__main__":
    t1 = TreeNode(2)
    t2 = TreeNode(1)
    t3 = TreeNode(5)
    t4 = TreeNode(6)
    t5 = TreeNode(9)
    t6 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t2.left = t5
    t2.right = t6
    print(preTraversal(t1))
