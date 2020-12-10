#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：不同路径.py
@Author  ：Junhui Yu
@Date    ：2020/12/9 21:05
@一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1 for i in range(m)] for j in range(n)]
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]


s = Solution()
o = s.uniquePaths(3, 2)
print(o)
