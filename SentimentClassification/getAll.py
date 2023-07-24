import pandas as pd
import sys
import io
import torch
from torch.utils.data import Dataset
from transformers import BertTokenizerFast, BertModel

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

CsvPath = sys.argv[1]


class MyDataset(Dataset):
    def __init__(self, data_dir):
        df = pd.read_csv(data_dir, header=None)
        self.n_samples = df.shape[0]
        self.contents = df.values[:, :]

    def __getitem__(self, index):
        return self.contents[index]

    def __len__(self):
        return self.n_samples


textdata = MyDataset(CsvPath)

berTokenizer = BertTokenizerFast.from_pretrained("bert-base-chinese",
                                                 add_special_tokens=False,
                                                 do_lower_case=True)
bertModel = BertModel.from_pretrained('bert-base-chinese')


def useModel(text):
    features = berTokenizer.encode_plus(text,
                                        add_special_tokens=False,
                                        padding="max_length",
                                        truncation=True,
                                        max_length=128,
                                        return_tensors='pt')

    outputs = bertModel(
        input_ids=features['input_ids'],
        token_type_ids=features['token_type_ids'],
        attention_mask=features['attention_mask']
    )
    embeddings = outputs.last_hidden_state
    embeddings = embeddings.to(device)

    model = torch.load("SentimentClassification/model.pth", map_location=torch.device('cpu'))
    out = model(embeddings)
    maxIndex = torch.argmax(out, dim=1)
    if maxIndex == 0:
        return 0
    elif maxIndex == 1:
        return 1


Positive = 0
Negative = 0

if __name__ == '__main__':
    for index in range(textdata.__len__()):
        textString = str(textdata.__getitem__(index).tolist())
        textString = textString[2:-2]
        emotion = useModel(textString)
        if emotion == 0:
            Positive += 1
        else:
            Negative += 1
    print(Positive)
    print(Negative)
