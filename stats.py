
def calculateAccuracy(original, predicted):	
    TP=0; TN=0; FP=0; FN=0
    #countFalse=0
    #countTrue=0
    if len(original) <> len(predicted):
        return
    for i in range(len(original)):
        #print original[i],predicted[i] 
        if original[i] == predicted[i]:
            #countTrue=countTrue+1
            if original[i] == 1:
                TP+=1
            else:
                TN+=1
        else:
            #countFalse = countFalse+1
            if predicted[i] == 0:
                FN+=1
            else:
                FP+=1
    printStats(TP,FP,TN,FN,len(original)) #print the values

def printStats(TP,FP,TN,FN,total):
    accuracy = float(TP+TN)/total
    print "\nAccuracy:  " , accuracy*100
    print "\n"
    print "-----------Confusion matrix-----------------------------------"
    print "\n            PredictedNo       PredictedYes"
    print "\nActualNo      ",TN,"            ",FP
    print "\nActaulYes     ",FN,"            ",TP,"\n"
    print "--------------------------------------------------------------"
