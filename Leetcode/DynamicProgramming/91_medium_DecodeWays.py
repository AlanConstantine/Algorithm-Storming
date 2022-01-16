# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-14 22:17:03

# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

# 题目数据保证答案肯定是一个 32 位 的整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        dp = [0 for i in range(size+1)]  # 前i个字母可以组成多少种解码
        dp[0] = 1
        for i in range(1, size+1):
            if s[i-1] != '0':  # 如果该数字可以被编码,则其组成的方案和i-1相同,自己举例子验证下就知道了

                dp[i] += dp[i-1]
            # 如果当前数字可以和前一个数字一起编码,即捆绑计算方案,则与i-2的方案相同,即将s[i-2:i]编码的情况与s[i-2]的情况当作同一个字母等同对待
            if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


s = "226"
print(Solution().numDecodings(s))
