#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：20. 有效的括号.py
@Author  ：Junhui Yu
@Date    ：2020/12/10 22:40
@给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for i in s:
            if stack and i in dic:
                if dic[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
s=Solution()
o=s.isValid("()[]{}")
print(o)