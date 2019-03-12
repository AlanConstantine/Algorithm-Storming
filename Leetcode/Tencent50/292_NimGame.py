# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-03-11 20:29:47


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

# 一个找规律的题，挺有意思的：
# 当我拿完还剩1、2、3个时，必败，故我拿前有4个时必败，
# 所以只要在我拿前有5、6、7个时，
# 就可以必胜（5个时拿走一个，6拿2，7拿3，使对手转入拿前4个的必败状态），
# 所以我拿前还有8个时必败（使对手转入必胜的拿前5、6、7状态）... ...
