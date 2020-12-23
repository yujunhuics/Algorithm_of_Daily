#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：387. 字符串中的第一个唯一字符.py
@Author  ：Junhui Yu
@Date    ：2020/12/23 16:54 
'''


# 1、超时代码
# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s == '':
#             return -1
#         else:
#             count = []
#             for i in s:
#                 count.append(s.count(i))
#             print(count)
#
#             for i in range(len(count)):
#                 if min(count) > 1:
#                     return -1
#                 if count[i] == 1:
#                     return i

# 2、最早少加了return -1
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

#3、
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency=collections.Counter(s)
        print(frequency)
        for i,ch in enumerate(s):
            # print(i,ch)
            if frequency[ch]==1:
                return i
        return -1



s = Solution()
# o = s.firstUniqChar("")
# o = s.firstUniqChar("cc")
# o = s.firstUniqChar("leetcode")
o = s.firstUniqChar("loveleetcode")
# o = s.firstUniqChar("dddccdbba")

print(o)
