import torch
import torch.nn as nn
import numpy as np
import sys
from public.decoder.NetworkStructure.LSTM import LSTM
from public.decoder.NetworkStructure.trainer import Trainer

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Decode:
    def __init__(self, num_classes = 2):
        self.input_size = 768
        self.hidden_size = 128
        self.num_layers = 2
        self.num_epochs = 100
        self.learning_rate = 0.01
        self.DropOut = 0.5
        self.num_classes = num_classes
    
    def train(self, dataPath, labelsPath, modelPath):
        # 训练集
        data_train = np.load(dataPath)
        labels_train = np.load(labelsPath)

        # 实例化模型结构
        model = LSTM(self.input_size, 
                     self.hidden_size, 
                     self.num_layers, 
                     self.num_classes, 
                     self.DropOut).to(device)

        
        # 定义损失函数 优化器
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.learning_rate)

        # 实例化训练器
        # 参数 num_epochs  model  criterion  optimizer
        trainer = Trainer(self.num_epochs, model, criterion, optimizer)

        # 开始训练
        trainer.train(data_train, labels_train)  # 参数data_train  labels_train
        
        trainer.save(modelPath)    # 保存路径为 model.path