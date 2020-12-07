#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：单链表的排序.py
@Author  ：Junhui Yu
@Date    ：2020/12/7 22:18 
'''

#API
# class Solution:
#     def sortInList(self, head):
#         return sorted(head)
#

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head node
# @return ListNode类

#
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def sortInList(self, head):
#         li=[]
#
#
#         return sorted(head)

# s = Solution()
# o = s.sortInList([2, 1, 3])
# # o = s.sortInList([-426572,-406609,724427,-157789,-132713,720732,-39078,-348926,-693458,559374,114739,-748249,428207,-767407,401563,646432,-682870,483610,-608888,94840,749542,359115,131739,935294,347325,80573,-869091,-757897,-860166,-227942,-484068,-170790,-362441,-860466,819197,817675,886101,463504,-100482,496406,-860791])
# print(o)

class Solution:
    def sortInList(self , head ):
        # write code here
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        l.sort()
        p = head
        i = 0
        while p:
            p.val = l[i]
            i += 1
            p = p.next
        return head

