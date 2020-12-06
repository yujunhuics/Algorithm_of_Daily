#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：最小的k个数.py
@Author  ：Junhui Yu
@Date    ：2020/12/6 19:19
@题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here

        tinput=sorted(tinput)
        if len(tinput)>=k:
            output=tinput[:k]
        else:
            output=[]
        return output

s=Solution()
o=s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10)
print(o)

