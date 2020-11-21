#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：newcode.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 13:57 
'''
while True:
    try:
        s = input()
        result = ""
        for i in range(len(s)):
            start = max(0, i-len(result)-1)
            temp = s[start: i+1]
            if temp == temp[::-1]:
                result = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    result = temp
        if result:
            print(len(result))
    except:
        break