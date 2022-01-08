# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-08 15:50:28

# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

#  

# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  

# 提示：

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def wordBreak(self, s: str, wordDict) -> bool:
        size = len(s)
        dp = [False] * (size+1)
        dp[0] = True
        for i in range(size):
            for j in range(i+1, size+1):
                sub = s[i:j]
                if sub in wordDict and dp[i]:
                    dp[j] = True
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        size = len(s)
        dp = [False for _ in range(size+1)]
        dp[0] = True
        for i in range(1, size+1):
            for w in wordDict:
                if dp[i-len(w)] and w == s[i-len(w):i]:
                    dp[i] = True
        return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
print(Solution().wordBreak(s, wordDict))
