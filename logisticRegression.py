import pandas as pd
from math import exp
import stats

def predictClass(record, weights, rangeList):
    #print weights[0]
    #print record	
    ypredicted = weights[0]
    for i in rangeList:#range(len(weights)-1):
        #print weights[i+1],record[i]
	ypredicted += weights[i+1]*(record[i])
    #print 'ypredicted',ypredicted,exp(-ypredicted)	
    value = 1.0/float(1+exp(-ypredicted))
    #print 'value: ',value
    return value	


def getWeights(trainData,testData,learningFactor,numToConverge, weights,columns,rangeList):
    #Using batch stochastic gradient Ascent
    #print weights[0]
    for i in range(numToConverge):
	gradient = [0.0] * (columns - 1) # -1 to exclude class label
	for index in range(len(trainData)):
		row = [int(m) for m in trainData[index]]
		#row = [int(m) for m in row]
		ypredict = predictClass(row,weights, rangeList)
		error = row[-1]-ypredict
		#print error
		for k in range(len(row)-1):       #-1 to exclude class label
			gradient[k]=error*row[k]
	#weights = [weights[j]+gradient[j]*learningFactor for j in range(len(gradient)) ]	
		weights[0]+=learningFactor*error
		#print weights[0]
	    	for j in range(len(gradient)):
			weights[j+1]+=learningFactor*gradient[j]
		#print weights[0]
    return weights

def startLogisticRegression(trainData,testData):
    columns = len(trainData[0])
    weights = [0.0]*columns 	#-1 is not done as w0 is also added
    predicted = []
    actual=[]	
    # calculate co-efficents
    rangeList = [i for i in range(len(weights)-1)]	
    weights = getWeights(trainData,testData,0.81,100,weights,columns,rangeList)
    #weights = [round(weights[i],3) for i in range(len(weights))]	
    #print weights	
    # predict label
    print len(testData)	
    for row in testData:
	#print row
	row = [int(m) for m in row]
	#print row
	ypredict = predictClass(row,weights,rangeList)
	#print row[-1], ypredict, round(ypredict)
	predicted.append(round(ypredict))
	actual.append(row[-1]) 
        #for k in range(len(row)):
		#print row[k],
	#print 'end row'

    #calculate stats
    stats.calculateAccuracy(actual,predicted)
