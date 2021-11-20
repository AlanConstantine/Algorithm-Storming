# 我们从二叉树的根节点 root 开始进行深度优先搜索。

# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

# 如果节点只有一个子节点，那么保证该子节点为左子节点。

# 给出遍历输出 S，还原树并返回其根节点 root。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def recoverFromPreorder(self, traversal: str):
        if len(traversal) == 0:
            return None

        def help(tr, depth):
            if len(tr) == 0:
                return None
            getnum = ''
            for j in tr:
                if j == '-':
                    break
                else:
                    getnum += j
            root = TreeNode(int(getnum))
            tr = tr[len(getnum)+depth:]
            num_ = 0
            p1 = len(tr)
            for i in range(len(tr)-1):
                if tr[i] == '-':
                    num_ += 1
                if tr[i] == '-' and tr[i+1] != '-':
                    if num_ == depth:
                        p1 = i + 1
                        break
                if tr[i] != '-':
                    num_ = 0
            root.left = help(tr[:p1], depth+1)
            root.right = help(tr[p1:], depth+1)
            return root

        return help(traversal, 1)


class Solution:
    def recoverFromPreorder(self, traversal: str):
        values = traversal.split("-")
        root = TreeNode(int(values[0]))
        # 利用nodes来记录先访问的左节点，方便后面的节点来找父节点,当左侧节点访问结束后访问右侧节点时用右侧节点替换左侧节点的位置
        nodes = [root]
        count = 0
        for val in values[1:]:
            if val == "":
                count += 1
            else:
                new_node = TreeNode(int(val))
                if nodes[count].left is None:  # 根据count来寻找父节点，如果父节点的left存在了，则放到右节点上
                    nodes[count].left = new_node
                else:
                    nodes[count].right = new_node
                if len(nodes) <= count + 1:  # 根据count来放节点，方便后面节点找父节点
                    nodes.append(new_node)
                else:
                    # 如果count+1存在节点，则说明此次的节点为右侧节点，替换原来的左节点作为后面节点的父节点
                    nodes[count + 1] = new_node
                count = 0
        return root


def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res


in_ = "1-2--3--4-5--6--7"
# in_ = "1-2--3---4-5--6---7"
in_ = "1-401--349---90--88"
a = Solution().recoverFromPreorder(in_)
print(inorder(a))
