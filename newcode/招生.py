#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Algorithm_of_Daily 
@File    ：招生.py
@Author  ：Junhui Yu
@Date    ：2020/11/22 19:13 
'''
while True:
    try:
        n,m,p=input().split()
        gaokao=[]
        xiao=[]
        # print(n,m,p)
        for i in range(int(n)):
            # gaokao_s=input()
            # xiao_s=input()
            gaokao_s,xiao_s=input().split()
            gaokao.append(int(gaokao_s))
            xiao.append(int(xiao_s))
        # print(xiao)
        # for i in range(int(n)):
        #     print(gaokao[i],xiao[i])
        zhaosheng=[i for i in range(int(m))]
        # print(len(zhaosheng))
        all_s=[]
        for i in range(int(n)):
            sum=gaokao[i]*0.85+xiao[i]*0.15
            all_s.append(sum)
        # print(all_s)
        all_s=sorted(all_s,reverse=True)
        zhaosheng=all_s[:int(m)]
        # print(zhaosheng)
        xiao_A=0
        for i in range(0,751):
            if i*0.85+750*0.15>min(zhaosheng):
                xiao_A=i
                break
        print(xiao_A)

        # xiao_A*0.85+750*0.15>min(zhaosheng)
        # print(int((min(zhaosheng)-750*0.15)/0.85)+1)
        # print(672*0.85+750*0.15)
    except:
        break