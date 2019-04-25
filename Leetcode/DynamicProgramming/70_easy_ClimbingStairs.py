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


S = Solution()
print(S.climbStairs(5))
