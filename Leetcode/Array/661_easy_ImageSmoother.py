# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Array'))
    print(os.getcwd())
except:
    pass

# %%
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

# 示例 1:

# 输入:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# 输出:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 注意:

# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。


# %%
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        sum_ = 0
        count = 1
        row = len(M)
        col = len(M[0])
        resM = [[0 for c in range(col)] for r in range(row)]
        for r in range(row):
            for c in range(col):
                sum_ = M[r][c]
                if r-1 >= 0:
                    sum_ += M[r-1][c]
                    count += 1
                if c-1 >= 0:
                    sum_ += M[r][c-1]
                    count += 1
                if r-1 >= 0 and c-1 >= 0:
                    sum_ += M[r-1][c-1]
                    count += 1
                if r+1 < row:
                    sum_ += M[r+1][c]
                    count += 1
                if c+1 < col:
                    sum_ += M[r][c+1]
                    count += 1
                if c+1 < col and r+1 < row:
                    sum_ += M[r+1][c+1]
                    count += 1
                if r-1 >= 0 and c+1 < col:
                    sum_ += M[r-1][c+1]
                    count += 1
                if r+1 < row and c-1 >= 0:
                    sum_ += M[r+1][c-1]
                    count += 1

                resM[r][c] = int(sum_/count)
                count = 1
        return resM


# %%
A = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
s = Solution()
s.imageSmoother(A)


# %%
int(0.74)
