# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-16 16:49:42

# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。

# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。

#  

# 示例 1：

# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
# 示例 2：

# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# refer: https://leetcode-cn.com/problems/ugly-number-ii/solution/fu-xue-ming-zhu-gai-shui-cheng-yi-2-3-5-92zlw/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 丑数因数一定只含 2，3，5，所以丑数 * 2 or 3 or 5也一定是丑数
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2*dp[index2], 3*dp[index3], 5*dp[index5])
            if dp[i] == 2 * dp[index2]:
                index2 += 1
            if dp[i] == 3*dp[index3]:
                index3 += 1
            if dp[i] == 5*dp[index5]:
                index5 += 1
        return dp[-1]


n = 10
print(Solution().nthUglyNumber(n))
