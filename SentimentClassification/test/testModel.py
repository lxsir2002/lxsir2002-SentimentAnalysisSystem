import torch
import numpy as np
import torch.nn as nn

model = torch.load("../ProductReviews/models/model.pth")
model.eval()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 测试集
data_test = np.load("../ProductReviews/data/PreData/TestEmbeddingsList.npy")
labels_test = np.load("../ProductReviews/data/PreData/TestLabelsList.npy")

ans = []
for i, (features, labels) in enumerate(zip(data_test, labels_test)):
    features_tensor = torch.tensor(features).float().to(device)
    labels_tensor = torch.tensor(labels).long().to(device)
    out = model(features_tensor)
    ans.append(torch.sum(labels_tensor == torch.argmax(out, dim=1)) / 64)

print(ans)