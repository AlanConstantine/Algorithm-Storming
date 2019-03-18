# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-18 21:35:06

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321
# 示例 3:

# 输入: 120
# 输出: 21
# 注意:

# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1
        if x < 0:
            f = -1
            x = -1*x
        if x == 0:
            return 0
        tmp_x = x
        k = 0
        while tmp_x > 0:
            k = k*10+tmp_x % 10
            tmp_x = tmp_x//10
        if -2**31 <= k <= (2**31-1):
            return k if f > 0 else -1*k
        else:
            return 0


s = Solution()
print(s.reverse(-123))
