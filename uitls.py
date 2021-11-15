class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, val):
        q = Node(val)
        if not self.is_empty():
            self.rear.next = q
            self.rear = q
        else:
            self.head = q
            self.rear = q

    def dequeue(self):
        if not self.is_empty():
            res = self.head.val
            self.rear = self.head.next
            return res
        else:
            print('Empty queue.')


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        elem = self.items.pop()
        return elem

    def get_len(self):
        return len(self.items)

    def get_sum(self):
        sum = 0
        for item in self.items:
            sum += item.val
        return sum

    def show(self):
        show_ = []
        for item in self.items:
            show_.append(item.val)
        print(show_)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
