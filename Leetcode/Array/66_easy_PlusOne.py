# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-10-23 19:22:53


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            i = len(digits)-1

            def decimal(i):
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                else:
                    if digits[i-1] == 9:
                        digits[i] = 0
                        decimal(i-1)
                    else:
                        digits[i] = 0
                        digits[i-1] = digits[i-1]+1
            decimal(i)
        else:
            digits[-1] = digits[-1]+1
        return digits


class Solution2:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1
        ret = []
        for d in digits[::-1]:
            v = d+plus
            if v > 9:
                v = 0
                plus = 1
            else:
                plus = 0
            ret.insert(0, v)
        if plus == 1:
            ret.insert(0, 1)
        return ret


def main():
    S = Solution2()
    print(S.plusOne([9, 9, 9, 9]))


if __name__ == '__main__':
    main()
