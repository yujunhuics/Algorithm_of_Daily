#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：进制转换.py
@Author  ：Junhui Yu
@Date    ：2020/12/7 22:43
@题目描述
给定一个十进制数M，以及需要转换的进制数N。将十进制数M转化为N进制数
'''
#复杂度太大
# class Solution:
#     def solve(self , M , N ):
#         s=''
#         temp=0
#         while M!=0:
#             s+=str(M%N)
#             M=M//N
#         return s


#
# 进制转换
# @param M int整型 给定整数
# @param N int整型 转换到的进制
# @return string字符串
#
class Solution:
    def solve(self, M, N):

        hash_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        # write code here
        if M < 0:
            curr = -M
        else:
            curr = M
        result = []
        while curr > 0:
            last = int(curr / N)
            mod = curr % N
            result.append(str(mod) if mod < 10 else hash_map[mod])
            curr = last
        result.reverse()
        if M < 0:
            return '-' + ''.join(result)
        else:
            return ''.join(result)



s=Solution()
o=s.solve(7,2)
print(o)
