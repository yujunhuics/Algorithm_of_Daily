#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：买卖股票的最好时机.py
@Author  ：Junhui Yu
@Date    ：2020/12/9 11:03
@题目描述
假设你有一个数组，其中第\ i i 个元素是股票在第\ i i 天的价格。
你有一次买入和卖出的机会。（只有买入了股票以后才能卖出）。请你设计一个算法来计算可以获得的最大收益
'''


class Solution:
    def maxProfit(self, prices):
        maxP = 0
        temp = 0
        if prices == []:
            maxP = 0
            return maxP
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                temp = prices[j] - prices[i]
                if temp > maxP:
                    maxP = temp
                else:
                    maxP = maxP

        return maxP


s = Solution()
o = s.maxProfit([2, 1])
print(o)
