#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：net_NER 
@File    ：dataset.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 19:21 
'''
import torch
from torch.utils.data import Dataset, DataLoader
import os
import re

"""
完成数据集准备
"""
TRAIN_PATH = r"aclImdb\train"
TEST_PATH = r"aclImdb\test"


# 分词
def tokenlize(content):
    content = re.sub(r"<.*?>", " ", content)
    filters = ['!','"','#','$','%','&','\(','\)','\*','\+',',','-','\.','/',':',';','<','=','>','\?','@'
        ,'\[','\\','\]','^','_','`','\{','\|','\}','~','\t','\n','\x97','\x96','”','“',]
    content = re.sub("|".join(filters), " ", content)
    tokens = [i.strip().lower() for i in content.split()]
    return tokens


class ImbdDateset(Dataset):
    def __init__(self, train = True):
        self.train_data_path = TRAIN_PATH
        self.test_data_path = TEST_PATH
        # 通过train和data_path控制读取train或者test数据集
        data_path = self.train_data_path if train else self.test_data_path
        # 把所有文件名放入列表
        # temp_data_path = [data_path + '/pos', data_path + '/neg']
        temp_data_path = [os.path.join(data_path , 'pos'), os.path.join(data_path , 'neg')]
        self.total_file_path = []  # 所有pos,neg评论文件的path
        # 获取每个文件名字，并拼接路径
        for path in temp_data_path:
            file_name_list = os.listdir(path)
            file_path_list = [os.path.join(path, i) for i in file_name_list if i.endswith('.txt')]
            self.total_file_path.extend(file_path_list)


    def __getitem__(self, index):
        # 获取index的path
        file_path = self.total_file_path[index]
        # 获取label
        label_str = file_path.split('\\')[-2]
        label = 0 if label_str =='neg' else 1
        # 获取content
        tokens = tokenlize(open(file_path, errors='ignore').read())
        return tokens, label


    def __len__(self):
        return len(self.total_file_path)

def get_dataloader(train = True):
    imdb_dataset = ImbdDateset(train)
    data_loader = DataLoader(imdb_dataset, shuffle = True, batch_size = 128, collate_fn = collate_fn)
    return data_loader

# 重新定义collate_fn
def collate_fn(batch):
    """
    :param batch: (一个__getitem__[tokens, label], 一个__getitem__[tokens, label],..., batch_size个)
    :return:
    """
    content, label = list(zip(*batch))
    from lib import ws, max_len
    content = [ws.transform(i, max_len = max_len) for i in content]
    content = torch.LongTensor(content)
    label = torch.LongTensor(label)
    return content, label


if __name__ == '__main__':
    for idx, (input, target) in enumerate(get_dataloader()):
        print(idx)
        print(input)
        print(target)
        break

