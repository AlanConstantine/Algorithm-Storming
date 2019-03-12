# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-11 22:51:27

# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例 1:

# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        words = s.split()
        for w in words:
            res.append(w[::-1])
        return ' '.join(res)


s = "Let's take LeetCode contest"
