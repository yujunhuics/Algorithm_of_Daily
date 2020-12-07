#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：最长无重复字串.py
@Author  ：Junhui Yu
@Date    ：2020/12/7 11:02
@题目描述
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
'''


# 超时的代码
# class Solution:
#     def maxLength(self, arr):
#
#         count = 0
#         if len(arr) == len(set(arr)):
#             count = len(arr)
#         else:
#             for i in range(len(arr)):
#                 temp = []
#                 for j in range(i, len(arr)):
#                     if arr[j] not in temp:
#                         temp.append(arr[j])
#                     else:
#                         break
#                 if count < len(temp):
#                     count = len(temp)
#                 else:
#                     count = count
#
#         return count

# 通过的代码
class Solution:
    def maxLength(self, arr):
        hash_set = set()
        cur_len = 0
        left = 0
        max_len = 0
        for i in arr:
            while i in hash_set:
                hash_set.remove(arr[left])
                cur_len -= 1
                left += 1
            hash_set.add(i)
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len


s = Solution()
# o = s.maxLength([2, 3, 4, 5])
o = s.maxLength([2, 1, 2, 3, 4, 5, 3])
print(o)

# s=set([1,2,3,4])
# print(s)
# s.clear()
# print(s)
