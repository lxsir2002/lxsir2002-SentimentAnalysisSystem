import torch


class Trainer:
    def __init__(self, num_epochs, model, criterion, optimizer):
        self.num_epochs = num_epochs
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer

    def train(self, data_train, labels_train):
        print("开始训练")
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        for epoch in range(self.num_epochs):
            for i, (features, labels) in enumerate(zip(data_train, labels_train)):
                features_tensor = torch.tensor(features).float().to(device)
                labels_tensor = torch.tensor(labels).long().to(device)
                out = self.model(features_tensor)
                loss = self.criterion(out, labels_tensor)
                loss.backward()
                self.optimizer.step()
                self.optimizer.zero_grad()

            print('Epoch:', '%04d' % (epoch + 1), 'loss =', '{:.6f}'.format(loss))

    def save(self, path):
        torch.save(self.model, path)
        print("模型保存完成")
