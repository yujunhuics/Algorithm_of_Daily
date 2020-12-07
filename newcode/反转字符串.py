#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：反转字符串.py
@Author  ：Junhui Yu
@Date    ：2020/12/7 21:27
@题目描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
'''


class Solution:
    def solve(self, str):
        return str[::-1]


s = Solution()
o = s.solve('zdsad')
print(o)
