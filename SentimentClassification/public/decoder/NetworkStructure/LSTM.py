import torch
import torch.nn as nn
import torch.nn.functional as F

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes, DropOut):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_classes = num_classes
        self.DropOut = DropOut
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True,
                            bidirectional=True,
                            dropout=self.DropOut)
        self.fc = nn.Linear(hidden_size * 2, self.num_classes)

    def attention_net(self, lstm_output, final_state):
        
        hidden = torch.cat((final_state[0], final_state[1]), dim=1).unsqueeze(2)

        attn_weights = torch.bmm(lstm_output, hidden).squeeze(2)

        soft_attn_weights = F.softmax(attn_weights, 1)

        context = torch.bmm(lstm_output.transpose(1, 2), soft_attn_weights.unsqueeze(2)).squeeze(2)

        return context, soft_attn_weights

    def forward(self, inputs):
        h0 = torch.randn(self.num_layers * 2, inputs.size(0), self.hidden_size).to(device)
        c0 = torch.randn(self.num_layers * 2, inputs.size(0), self.hidden_size).to(device)
        output, (final_hidden_state, final_cell_state) = self.lstm(inputs, (h0, c0))
        attn_output, attention = self.attention_net(output, final_hidden_state)
        return self.fc(attn_output)
