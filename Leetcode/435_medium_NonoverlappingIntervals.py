# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

# 注意:

# 可以认为区间的终点总是大于它的起点。
# 区间[1, 2] 和[2, 3] 的边界相互“接触”，但没有相互重叠。

# 示例 1:

# 输入: [[1, 2], [2, 3], [3, 4], [1, 3]]

# 输出: 1

# 解释: 移除[1, 3] 后，剩下的区间没有重叠。
# 示例 2:

# 输入: [[1, 2], [1, 2], [1, 2]]

# 输出: 2

# 解释: 你需要移除两个[1, 2] 来使剩下的区间没有重叠。
# 示例 3:

# 输入: [[1, 2], [2, 3]]

# 输出: 0

# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

# 仅需要考虑根据右端排序后的区间右端小于左端
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: x[1])  # 根据右端进行排序

        right = intervals[0][1]  # 记录第一个区间的右端
        ans = 1  # 记录保留的区间数，因为至少有一个区间，所以初始值是1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:  # 判断下一个区间的左端是否大于等于上一个区间的右端
                ans += 1  # 是则保留，ans+1
                # 并且right更换当前区间的右端给下一个区间的左端进行判断
                # （如果不满足if，right继续保留上一个区间的右端，当前区间则是要舍弃的，即不被ans记录）
                right = intervals[i][1]
        return len(intervals) - ans


a = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(Solution().eraseOverlapIntervals(a))
