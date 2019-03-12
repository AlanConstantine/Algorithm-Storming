# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Array'))
    print(os.getcwd())
except:
    pass

# %%
# 如果数组是单调递增或单调递减的，那么它是单调的。

# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

# 当给定的数组 A 是单调数组时返回 true，否则返回 false。


# 示例 1：

# 输入：[1,2,2,3]
# 输出：true
# 示例 2：

# 输入：[6,5,4,4]
# 输出：true
# 示例 3：

# 输入：[1,3,2]
# 输出：false
# 示例 4：

# 输入：[1,2,4,5]
# 输出：true
# 示例 5：

# 输入：[1,1,1]
# 输出：true


# 提示：

# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000


# %%
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = 0
        decrease = 0
        equal = 0
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                increase += 1
            elif A[i-1] > A[i]:
                decrease += 1
            else:
                equal += 1
        if equal == len(A)-1 or increase == 0 or decrease == 0:
            return True
        else:
            return False


class Solution2:
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))


class Solution3:
    def isMonotonic(self, A):
        store = 0
        for i in range(len(A) - 1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True


# %%
A = [1, 2, 2, 3]


# %%
s = Solution2()
print(s.isMonotonic(A))
