#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：860. 柠檬水找零.py
@Author  ：Junhui Yu
@Date    ：2020/12/10 20:35
@在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
提示：
0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20

模拟 + 贪心
由于顾客只可能给你三个面值的钞票，而且我们一开始没有任何钞票，因此我们拥有的钞票面值只可能是 55 美元，1010 美元和 2020 美元三种。基于此，我们可以进行如下的分类讨论。
5 5 美元，由于柠檬水的价格也为 55 美元，因此我们直接收下即可。
10 10 美元，我们需要找回 55 美元，如果没有 55 美元面值的钞票，则无法正确找零。
20 20 美元，我们需要找回 1515 美元，此时有两种组合方式，一种是一张 1010 美元和 55 美元的钞票，一种是 33 张 55 美元的钞票，如果两种组合方式都没有，则无法正确找零。当可以正确找零时，两种找零的方式中我们更倾向于第一种，即如果存在 55 美元和 1010 美元，我们就按第一种方式找零，否则按第二种方式找零，因为需要使用 55 美元的找零场景会比需要使用 1010 美元的找零场景多，我们需要尽可能保留 55 美元的钞票。
基于此，我们维护两个变量 \textit{five}five 和 \textit{ten}ten 表示当前手中拥有的 55 美元和 1010 美元钞票的张数，从前往后遍历数组分类讨论即可。
作者：LeetCode-Solution
'''


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        flag=True
        for bill in bills:
            if bill == 5:
                five += 1
                flag=True
            elif bill == 10:
                if five == 0:
                    # return False
                    flag=False
                    break
                else:
                    five -= 1
                    ten += 1
                    flag=True
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # return True
                    flag=True
                elif five >= 3:
                    five -= 3
                    flag=True
                else:
                    # return False
                    flag=False
                    break
        return flag


s = Solution()
# o = s.lemonadeChange([5, 5, 10])
# o = s.lemonadeChange([5,5,10,10,20])
o = s.lemonadeChange([5,5,5,5,20,20,5,5,20,5])
print(o)
# #
# li=[1,2,3]
# s=li.pop()
# print(s)
