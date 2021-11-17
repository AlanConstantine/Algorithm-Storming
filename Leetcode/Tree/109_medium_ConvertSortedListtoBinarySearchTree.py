# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        linklist = self.iterlink(head)  # 链表转list

        def help(lst):
            # 取list中间点作为根节点进行递归
            if len(lst) == 0:
                return None
            if len(lst) == 1:
                return TreeNode(lst[0])
            mid = len(lst)//2
            root = TreeNode(lst[mid])
            root.left = help(lst[:mid])
            if mid+1 >= len(lst):
                root.right = None
            else:
                root.right = help(lst[mid+1:])
            return root

        return help(linklist)

    def iterlink(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


def buildlist(og):
    header = ListNode(og[0])
    pre = header
    for i in og[1:]:
        header.next = ListNode(i)
        header = header.next
    return pre


og = [-10, -3, 0, 5, 9]
print(buildlist(og).next.val)
