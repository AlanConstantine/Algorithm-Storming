# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。请注意，返回的下标值（index1 和 index2）不是从零开始的。

# 你可以假设每个输入都只有一个解决方案，而且你不会重复使用相同的元素。

# 输入：数组 = {2, 7, 11, 15}, 目标数 = 9
# 输出：index1 = 1, index2 = 2


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = None
        index2 = None
        for i in range(len(numbers)):
            sub = target - numbers[i]
            if i + 1 == len(numbers):
                break
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                print(left, right, mid)
                if target > 0 and numbers[mid] >= target:
                    right = mid - 1
                    continue
                if numbers[mid] == sub:
                    index1 = i + 1
                    index2 = mid + 1
                    return [index1, index2]
                if numbers[mid] < sub:
                    left = mid + 1
                else:
                    right = mid - 1
        return [index1, index2]


class Solution2:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexdict = {}
        for i, num in enumerate(numbers):
            if target - num in indexdict:
                return [indexdict[target - num] + 1, i + 1]
            indexdict[num] = i


numbers = [-1, 0]
target = -1
print(Solution2().twoSum(numbers, target))
