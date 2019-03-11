# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-11 21:43:06

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


# 示例 1：

# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：

# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 双指针，首位指向，相中间靠拢
        p = 0
        q = len(s)-1
        while p < q:
            s[q], s[p] = s[p], s[q]
            p += 1
            q -= 1


s = ["H", "a", "n", "n", "a", "h"]
solu = Solution()
solu.reverseString(s)
print(s)
