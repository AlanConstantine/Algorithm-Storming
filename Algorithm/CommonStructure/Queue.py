#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-28 22:59:21
# @Version : Python2.7
# @Author  : AlanLau
# @Email   : rlalan@outlook.com
# @Blog    : http://blog.csdn.net/AlanConstantineLau


class Queue:
    """docstring for ClassName"""

    def __init__(self):
        # super(ClassName, self).__init__()
        self.queue = []

    def size(self):
        return len(self.queue)

    def get(self):
        return self.queue.pop()

    def push(self, object):
        return self.queue.insert(0, object)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def show(self):
        return self.queue


def main():
    q = Queue()
    print q.isEmpty()
    q.push('alan')
    print q.show()
    q.push('1')
    print q.show()
    print q.get()
    print q.show()
    print q.size()


if __name__ == '__main__':
    main()
