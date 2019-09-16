# -*- coding: utf-8 -*-
# @Date    : 2017-07-19 22:48:02
# @Author  : AlanLau
# @Version : Ubantu16.04LTS Python2.7


import numpy as np


class LinearList():
    """docstring for ClassName"""

    def __init__(self):
        self.linear = []

    def isEmpty(self):
        '''if empty.'''
        if len(self.linear) == 0:
            return True
        else:
            return False

    def List_len(self):
        '''reutrn list's length.'''
        return len(self.linear)

    def get_element(self, i):
        '''get element which index is i'''
        if i >= len(self.linear) or i < 0:
            return '[error] index out of list range!'
        else:
            return self.linear[i]

    def List_locate(self, x):
        '''find element by element's value'''
        for i in xrange(len(self.linear)):
            if self.linear[i] == x:
                return i, x
        return 0

    def List_insert(self, x, i):
        '''insert x into position i.'''
        if i > len(self.linear) or i < 0:
            print('[error] insert error!')
        else:
            if i == len(self.linear):
                self.linear.append(x)
            else:
                lastone = self.linear[-1]
                self.linear.append(lastone)
                for index in range(len(self.linear)-1, i, -1):
                    self.linear[index] = self.linear[index-1]
                self.linear[i] = x

    def List_delete(self, i):
        '''delete element whose position is i.'''
        if i >= len(self.linear):
            print('[error] i bigger than list range')
        elif i < 1:
            print('[error] i smaller than 1')
        else:
            for index in range(i, len(self.linear)):
                if (index+1) >= len(self.linear):
                    break
                else:
                    self.linear[index] = self.linear[index+1]
            self.linear = self.linear[:-1]

    def get_List(self):
        return self.linear


def main():
    # linear = [1, 2]
    lls = LinearList()
    print(lls.isEmpty())
    lls.List_insert(2, 0)
    lls.List_insert(3, 1)
    lls.List_insert(5, 2)
    # print lls.get_List()
    lls.List_insert(9, 1)
    lls.List_insert(19, 1)
    print(lls.get_List())
    # lls.List_delete(1)
    lls.List_delete(1)
    print(lls.get_List())


if __name__ == '__main__':
    main()
