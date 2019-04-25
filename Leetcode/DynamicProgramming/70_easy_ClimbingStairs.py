# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-04-25 18:41:57

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


# 分析
# 递归式
# f(n)=f(n-1)+f(n-2)
# 结束条件
# if n=0, return 0;
# if n=1, return 1;
# if n=2, return 2;
# if n=3, return 3.

class Solution(object):
    def __init__(self):
        self.p = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return n
        if n not in self.p:
            steps = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.p[n] = steps
            return steps
        else:
            return self.p[n]


S = Solution()
print(S.climbStairs(5))
