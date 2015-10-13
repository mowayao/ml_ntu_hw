import numpy as np
import random
eps = 1e-8



def getSign(x):
    if x > eps:
        return 1
    else:
        return -1

def readData(fileName):
    X = []
    Y = []
    File = open(fileName)
    for line in File.readlines():
        a = map(float,line.split())
        a.insert(-1,1)
        Y.append(getSign(a[-1]))
        X.append(np.array(a[:-1]))
    return np.array(X),Y

def train(X,Y,maxIter = 50):
    cyc = random.sample(xrange(len(X)),len(X))
    n,m = X.shape
    maxT = 0
    cnt = 0
    w = np.zeros(m)
    tw = np.zeros(m)
    for i in cyc:
        if getSign(tw.dot(X[i])) != Y[i]:
            tw = tw + Y[i]*X[i]
            nt = test(tw,X,Y)
            if maxT < nt:
                w = tw
                maxT = nt
            cnt+=1
            if cnt == maxIter:
                break
    #print maxT
    return w
def test(w,X,Y):
    t = 0
    for i in xrange(len(X)):
        if getSign(X[i].dot(w)) == Y[i]:
            t += 1
    return t
def experment(T = 2000):
    trainX,trainY = readData("D:\\hw1_18_train.dat")
    testX,testY = readData("D:\\hw1_18_test.dat")
    sum = 0
    for i in xrange(T):
        random.seed(i)
        print i
        w = train(trainX,trainY,100)
        #print float(test(w,testX,testY))/len(testX)
        sum += float(test(w,testX,testY))/len(testX)
    print 1-sum/T

experment()
