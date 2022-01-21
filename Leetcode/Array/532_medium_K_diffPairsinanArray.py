# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2018-04-26 22:29:03

# 给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

# 这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：

# 0 <= i < j < nums.length
# |nums[i] - nums[j]| == k
# 注意，|val| 表示 val 的绝对值。

#  

# 示例 1：

# 输入：nums = [3, 1, 4, 1, 5], k = 2
# 输出：2
# 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2：

# 输入：nums = [1, 2, 3, 4, 5], k = 1
# 输出：4
# 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3：

# 输入：nums = [1, 3, 1, 5, 4], k = 0
# 输出：1
# 解释：数组中只有一个 0-diff 数对，(1, 1)。
# 示例 4：

# 输入：nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# 输出：2
# 示例 5：

# 输入：nums = [-1,-2,-3], k = 1
# 输出：2
#  

# 提示：

# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counter = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k and [nums[i], nums[j]] not in counter:
                    counter.append([nums[i], nums[j]])
        return len(counter)
    # Time out


class Solution1:
    def findPairs(self, nums, k: int) -> int:
        ans = 0
        if k == 0:
            temp = {}
            for n in nums:
                if n in temp:
                    temp[n] += 1
                else:
                    temp[n] = 1
            for k, v in temp.items():
                if v > 1:
                    ans += 1
            return ans
        nums.sort()
        pre = None
        while nums:
            n = nums.pop(0)
            if n == pre:
                continue
            pre = n
            if n+k in nums:
                ans += 1
            if n-k in nums:
                ans += 1
        return ans


class Solution:
    def findPairs(self, nums, k: int) -> int:
        res = set()  # 满足条件能形成的pair
        seen = set()  # 已经被遍历过的
        for num in nums:
            if num - k in seen:
                res.add((num-k, num))  # 按照小大顺序储存
            if num + k in seen:
                res.add((num, num+k))  # 按照小大顺序储存
            seen.add(num)
        return len(res)


k = 2
nums = [1, 3, 1, 5, 4]
# nums = [1, 1, 1, 1, 1, 2, 2]
print(Solution().findPairs(nums, k))
