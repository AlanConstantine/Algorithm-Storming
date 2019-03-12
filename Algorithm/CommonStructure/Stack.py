#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 22:46:03
# @Version : Python2.7
# @Author  : AlanLau
# @Email   : rlalan@outlook.com
# @Blog    : http://blog.csdn.net/AlanConstantineLau


class Stack:
    """a class to achieve stack"""

    def __init__(self):
        # super(Stack, self).__init__()
        self.items = []

    def push(self, item):
        """push an element to the top of stack"""
        self.items.append(item)

    def pop(self):
        """delete the element which is on the top of stack"""
        return self.items.pop()

    def peek(self):
        """get the top element"""
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.items[-1]

    def isEmpty(self):
        """is empty"""
        return len(self.items) == 0

    def size(self):
        """get the size of the stack"""
        return len(self.items)

    def show(self):
        return self.items


def main():
    stack = Stack()
    print stack.isEmpty()
    stack.push(4)
    print stack.show()
    stack.push('dog')
    print stack.show()
    print stack.peek()
    stack.push('True')
    print stack.size()
    print stack.isEmpty()
    stack.push(8.4)
    print stack.show()
    stack.pop()
    print stack.show()


if __name__ == '__main__':
    main()
