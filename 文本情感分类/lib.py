#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：net_NER 
@File    ：lib.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 19:21 
'''
import pickle
import torch

ws = pickle.load(open('./model/ws.pkl', 'rb'))

max_len = 200
embedding_dim = 100  # 用长度为100的向量表示一个词
hidden_size = 128  # 每个隐藏层中LSTM单元个数
num_layer = 2  # 隐藏层数量
bidirectional = True  # 是否双向LSTM
dropout = 0.3  # 在训练时以一定的概率使神经元失活，实际上就是让对应神经元的输出为0

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
