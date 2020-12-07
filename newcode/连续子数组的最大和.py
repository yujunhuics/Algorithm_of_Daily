#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：连续子数组的最大和.py
@Author  ：Junhui Yu
@Date    ：2020/12/7 21:03
@题目描述
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数
组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).
'''


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum = float('-inf')       #负无穷大
        # max_sum = sum(array)
        for i in range(len(array)):
            sumtemp = 0
            for j in range(i, len(array)):
                sumtemp += array[j]
                if sumtemp > max_sum:
                    max_sum = sumtemp
                else:
                    max_sum = max_sum
                    # break
        return max_sum


s = Solution()
o = s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
# o = s.FindGreatestSumOfSubArray([-2, -8, -1, -5, -9])
print(o)
