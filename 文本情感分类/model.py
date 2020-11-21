#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：net_NER 
@File    ：model.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 19:21 
'''
"""
定义模型
模型优化方法：
# 为使得结果更好 添加一个新的全连接层，作为输出，激活函数处理
# 把双向LSTM的output传给一个单向LSTM再进行处理

lib.max_len = 200
lib.embedding_dim = 100  # 用长度为100的向量表示一个词
lib.hidden_size = 128  # 每个隐藏层中LSTM单元个数
lib.num_layer = 2  # 隐藏层数量
lib.bidirectional = True  # 是否双向LSTM
lib.dropout = 0.3  # 在训练时以一定的概率使神经元失活，实际上就是让对应神经元的输出为0
lib.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
"""
import torch.nn as nn
from lib import ws, max_len
import torch.nn.functional as F
from torch.optim import Adam
from dataset import get_dataloader
from tqdm import tqdm
import torch
import numpy as np
import lib
import os


class Mymodel(nn.Module):
    def __init__(self):
        super(Mymodel, self).__init__()
        # nn.Embedding(num_embeddings - 词嵌入字典大小即一个字典里要有多少个词，embedding_dim - 每个词嵌入向量的大小。)
        self.embedding = nn.Embedding(len(ws), 100)
        # 加入LSTM
        self.lstm = nn.LSTM(input_size=lib.embedding_dim, hidden_size=lib.hidden_size, num_layers=lib.num_layer,
                            batch_first=True, bidirectional=lib.bidirectional, dropout=lib.dropout)
        self.fc = nn.Linear(lib.hidden_size * 2, 2)

    def forward(self, input):
        """
        :param input: 形状[batch_size, max_len]
        :return:
        """
        x = self.embedding(input)  # 进行embedding，形状[batch_size, max_len, 100]

        # x [batch_size, max_len, num_direction*hidden_size]
        # h_n[num_direction * num_layer, batch_size, hidden_size]
        x, (h_n, c_n) = self.lstm(x)
        # 获取两个方向最后一次的output(正向最后一个和反向第一个)进行concat
        # output = x[:,-1,:hidden_size]   前向，等同下方
        output_fw = h_n[-2, :, :]  # 正向最后一次输出
        # output = x[:,0,hidden_size:]   反向，等同下方
        output_bw = h_n[-1, :, :]  # 反向最后一次输出

        output = torch.cat([output_fw, output_bw], dim=-1)  # [batch_size, hidden_size*num_direction]

        out = self.fc(output)

        return F.log_softmax(out, dim=-1)


model = Mymodel()
optimizer = Adam(model.parameters(), lr=0.01)
if os.path.exists('./model/model.pkl'):
    model.load_state_dict(torch.load('./model/model.pkl'))
    optimizer.load_state_dict(torch.load('./model/optimizer.pkl'))


# 训练
def train(epoch):
    for idx, (input, target) in enumerate(get_dataloader(train=True)):
        output = model(input)
        optimizer.zero_grad()
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        print(loss.item())
        print('当前第%d轮,idx为%d 损失为:%lf, ' % (epoch, idx, loss.item()))

        # 保存模型
        if idx % 100 == 0:
            torch.save(model.state_dict(), './model/model.pkl')
            torch.save(optimizer.state_dict(), './model/optimizer.pkl')


# 评估
def test():
    acc_list = []
    loss_list = []
    # 开启模型评估模式
    model.eval()
    # 获取测试集数据
    test_dataloader = get_dataloader(train=False)
    # tqdm(total = 总数,ascii = #,desc=描述)
    for idx, (input, target) in tqdm(enumerate(test_dataloader), total=len(test_dataloader), ascii=True, desc='评估：'):
        with torch.no_grad():
            output = model(input)
            # 计算当前损失
            cur_loss = F.nll_loss(output, target)
            loss_list.append(cur_loss)
            pred = output.max(dim=-1)[-1]
            # 计算当前准确率
            cur_acc = pred.eq(target).float().mean()
            acc_list.append(cur_acc)
    print('准确率为:%lf, 损失为:%lf' % (np.mean(acc_list), np.mean(loss_list)))


if __name__ == '__main__':
    for i in tqdm(range(10)):
        train(i)
    test()
