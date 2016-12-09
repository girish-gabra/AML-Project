#import pandas as pd
import logisticRegression
import csv

def loadData(datapath):
    #dataFrame = pd.read_csv(datapath,sep=",")
    with open(datapath,'r') as f:
	dataList = list(csv.reader(f))[1:]
    return dataList
    

if __name__ == '__main__':
    trainDataPath = '/u/ggabra/AML Project/train3.csv'
    trainData =  loadData(trainDataPath)
    testDataPath = '/u/ggabra/AML Project/test_breast_cancer.csv'
    testData = loadData(testDataPath)
    print len(trainData), len(testData)	
    logisticRegression.startLogisticRegression(trainData,testData)
