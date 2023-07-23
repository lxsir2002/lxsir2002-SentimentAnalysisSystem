import torch
import sys
from transformers import BertTokenizerFast, BertModel
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

text = sys.argv[1]

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class useModdel:
    def __init__(self, text):
        self.text = text
    def start(self):
        berTokenizer = BertTokenizerFast.from_pretrained("bert-base-chinese",
                                                         add_special_tokens=False,
                                                         do_lower_case=True)
        bertModel = BertModel.from_pretrained('bert-base-chinese')

        features = berTokenizer.encode_plus(self.text,
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
        maxIdex = torch.argmax(out, dim=1)
        if (maxIdex == 0):
            return "Positive"
        elif (maxIdex == 1):
            return "Negative"




def startAnalyse(text):
    tools = useModdel(text)
    flage = tools.start()
    print(flage)
    return flage



startAnalyse(text)

