#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：net_NER 
@File    ：main.py
@Author  ：Junhui Yu
@Date    ：2020/11/21 19:21 
'''
# 由于pickle特殊性，需要在此导入Word2Sequence
from word_sequence import Word2Sequence
import pickle
import os
from dataset import tokenlize
from tqdm import tqdm  # 显示当前迭代进度

TRAIN_PATH = r"D:\资料\[0]课件\阶段9-人工智能NLP项目\第四天\代码\代码\data\aclImdb\train"


if __name__ == '__main__':
    ws = Word2Sequence()
    temp_data_path = [os.path.join(TRAIN_PATH, 'pos'), os.path.join(TRAIN_PATH, 'neg')]
    for data_path in temp_data_path:
        # 获取每一个文件的路径
        file_paths = [os.path.join(data_path, file_name) for file_name in os.listdir(data_path)]
        for file_path in tqdm(file_paths):
            sentence = tokenlize(open(file_path, errors = 'ignore').read())
            ws.fit(sentence)
    ws.build_vocab(max = 10, max_features = 10000)
    pickle.dump(ws, open('./model/ws.pkl', 'wb'))
    print(len(ws.dict))

