# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-14 20:57:20

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

#  

# 示例 1：


# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from turtle import left


class Solution1:
    # 第一次遍历向左扫一遍取每个位置的差值
    # 第二次逆向遍历向右扫一遍取每个位置的差值
    # 最后将两次遍历的结果取最小差值求和
    def trap(self, height) -> int:
        size = len(height)
        leftmax = [0] * size
        rightmax = [0] * size
        # get left max
        leftmaxvalue = float("-inf")
        rightmaxvalue = float("-inf")

        for i in range(size):
            leftmaxvalue = max(height[i], leftmaxvalue)
            leftmax[i] = leftmaxvalue - height[i]

        for i in range(size-1, -1, -1):
            rightmaxvalue = max(height[i], rightmaxvalue)
            rightmax[i] = rightmaxvalue - height[i]

        return sum([min(leftmax[i], rightmax[i]) for i in range(size)])


class Solution:
    # 双指针
    def trap(self, height) -> int:
        size = len(height)
        lefti = 0
        righti = size - 1
        ans = 0
        leftmaxvalue = 0
        rightmaxvalue = 0
        while righti > lefti:
            leftmaxvalue = max(leftmaxvalue, height[lefti])
            rightmaxvalue = max(rightmaxvalue, height[righti])
            if height[lefti] < height[righti]:
                ans += leftmaxvalue - height[lefti]
                lefti += 1
            else:
                ans += rightmaxvalue - height[righti]
                righti -= 1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]

print(Solution().trap(height))
