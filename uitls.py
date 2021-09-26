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
        pass
