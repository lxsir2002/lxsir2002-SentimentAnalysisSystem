import csv

with open("../data/SourceData/data1.txt", encoding="utf-8") as f:
    dataLines = f.readlines()

contents = []
labels = []

for dataLine in dataLines:
    dataLine = dataLine.strip()
    label = int(dataLine[-1])
    content = str(dataLine[:-1])
    content = content.replace('\t','')
    
    if(label != 1):
        if(label == 0):
            label = 1
        if(label == 2):
            label = 0
        
        contents.append(content)
        labels.append(label)

csv_reader = csv.reader(open("../data/SourceData/data2.csv", 'r', encoding="utf-8"))
for line in csv_reader:
    line = str(line)[2:-2]
    labels.append(1 - int(line[0]))
    contents.append(line[3:])

data = list(zip(labels, contents))

testData = data[0:int(len(data)/10)]
trainData = data[int(len(data)/10):]

with open('../data/PreData/TrainData.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['标签','内容'])
    writer.writerows(trainData)

with open('../data/PreData/TestData.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['标签', '内容'])
    writer.writerows(testData)

print("DataPreprocess is ok!")