#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：排序链表.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 14:37 
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head=sorted(head)
        return head

S=Solution()
head=[4,2,1,3]
head=S.sortList(head)
print(head)
