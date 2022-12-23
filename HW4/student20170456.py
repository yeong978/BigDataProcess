import numpy as np
import operator
import sys

trainingData = sys.argv[1]
testData = sys.argv[2]

def fileToMatrix(filename):
    f = open(filename)
    numberOfLines = len(f.readlines())
    returnMat = np.zeros((numberOfLines, 32))
    classLabelVector = []
    f = open(filename)
    index = 0
    for line in f.readlines():
        line = str.strip(line)
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat, classLabelVector

datingDataMat, datingLabels = fileToMatrix('datingTestSet.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

def createDataSet():
    trainingFileList = listdr('trainingDigits')
    m = len(trainingFileList)
    tMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        
        classfierResult = classify0(testMat, tMat, labels, 20)
        if classfierResult != classNumStr):
            errorCount += 1
        print(errorCount/mTest)
        print()
        

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

    

if __name__ == "__main__":
    group, labels = createDataSet()
    
    for i in range(1,21):
        result = classfy0(test, tMat, labels, i)
        print()
    
