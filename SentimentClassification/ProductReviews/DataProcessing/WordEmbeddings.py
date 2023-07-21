from public.encoder.GetBertWordEmbeddings import *

trainEmbeddingsList, trainLabelsList = GetBertWordEmbeddings("../data/PreData/TrainData.csv",
                                                                   batchSize = 64, 
                                                                   model = "bert-base-chinese")
SaveEmbeddingsAndLabels("../data/PreData/TrainEmbeddingsList.npy", trainEmbeddingsList, 
                        "../data/PreData/TrainLabelsList.npy", trainLabelsList)

TestEmbeddingsList, TestLabelsList = GetBertWordEmbeddings("../data/PreData/TestData.csv",
                                                                   batchSize = 64, 
                                                                   model = "bert-base-chinese")
SaveEmbeddingsAndLabels("../data/PreData/TestEmbeddingsList.npy", TestEmbeddingsList, 
                        "../data/PreData/TestLabelsList.npy", TestLabelsList)

print("GetBertWordEmbeddings is ok!")