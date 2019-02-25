# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-02-25 12:38:13

# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。

# 至少有一个空座位，且至少有一人坐在座位上。

# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

# 返回他到离他最近的人的最大距离。

# 示例 1：

# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
# 示例 2：
# [0,0,0,1]
# 输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。


# class Solution(object):
#     def maxDistToClosest(self, seats):
#         """
#         :type seats: List[int]
#         :rtype: int
#         """
#         endp = -1
#         count = 0
#         max_count = -1
#         for i in range(len(seats)):
#             if seats[i] == 0:
#                 count += 1
#                 if count >= max_count and endp-max_count+1 != 0:
#                     max_count = count
#                     endp = i
#             else:
#                 count = 0
#         if endp == len(seats)-1 or endp+1-max_count == 0:
#             return max_count
#         else:
#             return max_count//2 if max_count % 2 == 0 else max_count//2+1


# class Solution(object):
#     def maxDistToClosest(self, seats):
#         """
#         :type seats: List[int]
#         :rtype: int
#         """
#         max_ = 0
#         flag = -1
#         for i in range(len(seats)):
#             if seats[i] == 1:
#                 if flag == -1:
#                     max_ = i
#                 else:
#                     max_ = max((i-flag)/2, max_)
#                 flag = i
#         return max(max_, len(seats)-flag-1)


seats = [0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
s = Solution()
print(s.maxDistToClosest(seats))
