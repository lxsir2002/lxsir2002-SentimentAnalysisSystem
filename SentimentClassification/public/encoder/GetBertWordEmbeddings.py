import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizerFast, BertModel
import numpy

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class MyDataset(Dataset):
    def __init__(self, data_dir):
        df = pd.read_csv(data_dir)
        self.n_samples = df.shape[0]
        self.contents = df.values[:, 1]
        self.labels = df.values[:, 0]

    def __getitem__(self, index):
        return self.contents[index], self.labels[index]

    def __len__(self):
        return self.n_samples


def GetBertWordEmbeddings(path, batchSize, model="bert-base-chinese"):
    textDataset = MyDataset(path)
    dataLoader = DataLoader(textDataset, batch_size=batchSize)
    berTokenizer = BertTokenizerFast.from_pretrained(model,
                                                     add_special_tokens=False,
                                                     do_lower_case=True,)

    bertModel = BertModel.from_pretrained(model).to(device)

    embeddingsList = []
    labelsList = []

    for contents, labels in dataLoader:

        contents = list(contents)
        print(type(contents),len(contents), contents)
        features = berTokenizer.batch_encode_plus(contents,
                                                  add_special_tokens=False,
                                                  padding="max_length",
                                                  truncation=True,
                                                  max_length=128,
                                                  return_tensors='pt').to(device)

        outputs = bertModel(
            input_ids=features['input_ids'],
            token_type_ids=features['token_type_ids'],
            attention_mask=features['attention_mask']
        )

        embeddings = outputs.last_hidden_state  # 64 128 768
        del outputs

        embeddings = embeddings.cpu()  # 移至cpu，保证可以进行numpy()
        embeddingsList.append(embeddings.detach().numpy())
        labelsList.append(labels.numpy())
        del embeddings

    return embeddingsList[:-1], labelsList[:-1]


def SaveEmbeddingsAndLabels(EmbeddingsPath, EmbeddingsList, LabelsPath, LabelsList):
    numpy.save(EmbeddingsPath, EmbeddingsList)
    numpy.save(LabelsPath, LabelsList)

# trainEmbeddingsList, trainLabelsList = GetBertWordEmbeddings(".\\data\\TrainData.csv", batchSize = 64,
# model = "bert-base-chinese") SaveEmbeddingsAndLabels(".\\build\\TrainEmbeddingsList.npy", trainEmbeddingsList,
# ".\\build\\TrainLabelsList.npy", trainLabelsList)

# testEmbeddingsList, testLabelsList = GetBertWordEmbeddings(".\\data\\TestData.csv",batchSize = 64, model = "bert-base-chinese")
# SaveEmbeddingsAndLabels(".\\build\\TestEmbeddingsList.npy", testEmbeddingsList,
#                         ".\\build\\TestLabelsList.npy", testLabelsList)

# print("GetBertWordEmbeddings is ok!")
