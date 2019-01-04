# 链表反转（递归）


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head, newhead):
    tempnext = head.next
    head.next = newhead
    newhead = tempnext
    if newhead == None:
        return
    reverse(newhead, head)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4

print(n1.next.value)
print(n2.next.value)
print(n3.next.value)
print(n4.next)

reverse(n1, None)
print('After reverse:')
print(n4.next.value)
print(n3.next.value)
print(n2.next.value)
print(n1.next)
