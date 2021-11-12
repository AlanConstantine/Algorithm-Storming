# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

#  

# 示例：

# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9, 7, 8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

# 注意 在处理数组前，统计一遍信息（如频率、个数、第一次出现位置、最后一次出现位置等）可
# 以使题目难度大幅降低。

class Solution:
    def partitionLabels(self, s):
        if not s:
            return []
        lastpos = {k: i for i, k in enumerate(s)}  # 记录每个字母的最大下标值
        res = []
        j = lastpos[s[0]]  # 用j来记录首个字母的最大下标值
        num = 0
        for i in range(len(s)):
            num += 1
            j = max(j, lastpos[s[i]])
            # 如果当前字母的最大下标值小于被记录字母的最大下标值j，
            # 说明当前字母的依旧在重复出现的区间内，更新j为两个字母中的最大下标值最大的那一个
            # 关键思路：利用j来推进最大的下标指向（实时更新根据当前指针）
            if i == j:  # 如果当前指针等于最大下标值，说明指针到达了最多出现的临界点
                res.append(num)
                num = 0
        return res
