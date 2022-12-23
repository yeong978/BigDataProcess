#!/usr/bin/python3

import numpy as np
import operator
import os
import sys

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** .5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(fname):
    returnVect = np.zeros((1, 1024))
    with open(fname) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                returnVect[0, 32*i+j] = int(line[j])
    return returnVect

def classifier(trainingDataPath, testDataPath):
    trainingLabels = []
    trainingFileList = os.listdir(trainingDataPath)
    m = len(trainingFileList)
    trainingMats = np.zeros((m, 1024))
    for i in range(m):
        fname = trainingFileList[i]
        f = fname.split('.')[0]
        classNum = int(f.split('_')[0])
        trainingLabels.append(classNum)
        trainingMats[i, :] = file2matrix(os.path.join(trainingDataPath, fname))

    testLabels = []
    testFileList = os.listdir(testDataPath)
    m = len(testFileList)
    testMats = np.zeros((m, 1024))
    for i in range(m):
        fname = testFileList[i]
        f = fname.split('.')[0]
        classNum = int(f.split('_')[0])
        testLabels.append(classNum)
        testMats[i, :] = file2matrix(os.path.join(testDataPath, fname))

    for k in range(1, 21):
        error = 0
        resLabels = []
        for testLabel, testMat in zip(testLabels, testMats):
            res = classify0(testMat, trainingMats, trainingLabels, k)
            resLabels.append(res)
            if res != testLabel:
                error += 1
        errRate = error / len(testMats) * 100
        print(int(errRate))

if __name__ == '__main__':
    trainingDataPath = sys.argv[1]
    testDataPath = sys.argv[2]

    classifier(trainingDataPath, testDataPath)
