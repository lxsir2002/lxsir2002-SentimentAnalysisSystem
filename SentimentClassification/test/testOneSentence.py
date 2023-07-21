import torch
from transformers import BertTokenizerFast, BertModel

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

berTokenizer = BertTokenizerFast.from_pretrained("bert-base-chinese",
                                                 add_special_tokens=False,
                                                 do_lower_case=True)
bertModel = BertModel.from_pretrained('bert-base-chinese')

text = ""

while (True):
    text = input("请输入：")
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

    model = torch.load("../ProductReviews/models/model.pth")
    out = model(embeddings)

    maxIdex = torch.argmax(out, dim=1)
    print(out)
    if maxIdex == 1:
        print("负面评论")
    elif maxIdex == 0:
        print("正面评论")
