# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-03 08:56:41

# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。
# 也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
# 它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

# 车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），
# 然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。
# 另外，车不能与其他友方（白色）象进入同一个方格。

# 返回车能够在一次移动中捕获到的卒的数量。


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        steps = 0
        row = -1
        col = -1
        flag = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    row = i
                    col = j
                    flag = 1
                    break
            if flag == 1:
                break
        # Identify row
        R_row_str = ''.join(board[row]).replace('.', '')
        if 'Rp' in R_row_str:
            steps += 1
        if 'pR' in R_row_str:
            steps += 1

        # Identifu col
        # Upward
        for r in range(row-1, -1, -1):
            if board[r][col] not in '.p':
                break
            if board[r][col] == 'p':
                steps += 1
                break

        # Downward
        for r in range(row+1, len(board)):
            if board[r][col] not in '.p':
                break
            if board[r][col] == 'p':
                steps += 1
                break
        return steps


board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

board2 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "B", "R", "B", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]

board3 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          ["p", "p", ".", "R", ".", "p", "B", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "B", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]

s = Solution()
print(s.numRookCaptures(board3))
