# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-21 19:21:38

# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

#  

# 示例 1：

# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：

# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：

# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
#  

# 提示：

# 1 <= text1.length, text2.length <= 1000
# text1 和 text2 仅由小写英文字符组成。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        col, row = len(text1), len(text2)
        dp = [[0 for _ in range(col+1)]
              for _ in range(row+1)]  # 表示在以i和j下标前的公共子序列长度
        for r in range(1, row+1):
            for c in range(1, col+1):
                if text1[c-1] == text2[r-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]


text1 = "ps"
text2 = "vsh"
print(Solution().longestCommonSubsequence(text1, text2))
