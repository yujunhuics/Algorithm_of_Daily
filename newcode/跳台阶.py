#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：跳台阶.py
@Author  ：Junhui Yu
@Date    ：2020/12/8 13:07
@题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''


# 会超时
# class Solution:
#     def jumpFloor(self, number):
#         if number==0 or number==1:
#             return 1
#         else:
#             return self.jumpFloor(number-1)+self.jumpFloor(number-2)

class Solution:
    def jumpFloor(self, number):
        d1 = 1
        d2 = 1
        if number >= 2:
            for i in range(2, number + 1):
                t = d1 + d2
                d1 = d2
                d2 = t
        return d2


s = Solution()
o = s.jumpFloor(3)
print(o)
