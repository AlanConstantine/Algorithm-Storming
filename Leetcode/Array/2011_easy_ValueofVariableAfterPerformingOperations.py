# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-21 22:32:56

# 存在一种仅支持 4 种操作和 1 个变量 X 的编程语言：

# ++X 和 X++ 使变量 X 的值 加 1
# --X 和 X-- 使变量 X 的值 减 1
# 最初，X 的值是 0

# 给你一个字符串数组 operations ，这是由操作组成的一个列表，返回执行所有操作后， X 的 最终值 。

#  

# 示例 1：

# 输入：operations = ["--X","X++","X++"]
# 输出：1
# 解释：操作按下述步骤执行：
# 最初，X = 0
# --X：X 减 1 ，X =  0 - 1 = -1
# X++：X 加 1 ，X = -1 + 1 =  0
# X++：X 加 1 ，X =  0 + 1 =  1
# 示例 2：

# 输入：operations = ["++X","++X","X++"]
# 输出：3
# 解释：操作按下述步骤执行：
# 最初，X = 0
# ++X：X 加 1 ，X = 0 + 1 = 1
# ++X：X 加 1 ，X = 1 + 1 = 2
# X++：X 加 1 ，X = 2 + 1 = 3
# 示例 3：

# 输入：operations = ["X++","++X","--X","X--"]
# 输出：0
# 解释：操作按下述步骤执行：
# 最初，X = 0
# X++：X 加 1 ，X = 0 + 1 = 1
# ++X：X 加 1 ，X = 1 + 1 = 2
# --X：X 减 1 ，X = 2 - 1 = 1
# X--：X 减 1 ，X = 1 - 1 = 0

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
