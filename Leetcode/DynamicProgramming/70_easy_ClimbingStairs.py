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
# https://leetcode-cn.com/problems/climbing-stairs/


class SolutionI(object):
    def __init__(self):
        self.p = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        if n not in self.p:
            steps = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.p[n] = steps
            return steps
        else:
            return self.p[n]


class SolutionII(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        one_step_way = 1
        # 走一步
        two_step_way = 2
        # 走两步
        all_way = 0
        for i in range(2, n):
            all_way = one_step_way + two_step_way  # 当前状态仅和上一个状态和上上一个状态有关
            # 当all_way作为当前状态求出来之后
            one_step_way = two_step_way  # 上状态转移给上上状态
            two_step_way = all_way  # 当前状态转移给上状态
        return all_way

# 第n阶台阶只可能是从上一次跨台阶上来的
# 而上一次跨台阶可能是跨了1阶上到当前台阶，也可能是跨了2阶台阶到当前台阶
# 所以当前台阶的跨法是：f(n)=f(n-1)+f(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        s2 = 2
        s3 = 3
        sn = 0
        for i in range(3, n):
            sn = s3 + s2
            s2 = s3
            s3 = sn
        return sn


s = Solution()
print(s.climbStairs(12))
