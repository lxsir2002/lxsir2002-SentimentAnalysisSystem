from public.decoder.decode import *

decode = Decode(num_classes = 2)

decode.train("./data/PreData/TrainEmbeddingsList.npy", 
             "./data/PreData/TrainLabelsList.npy", 
             "./models/model.pth")
