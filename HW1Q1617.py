import numpy as np
import random

eps = 1e-8



def getSign(x):
    if x > eps:
        return 1
    else:
        return -1

def readData():
    X = []
    Y = []
    File = open("D:\\hw1_15_train.dat.txt")
    for line in File.readlines():
        a = map(float,line.split())
        a.insert(-1,1)
        Y.append(getSign(a[-1]))
        X.append(np.array(a[:-1]))
    return X,Y

def ISHALT(w,X,Y):
    for i in xrange(len(X)):
        if getSign(w.dot(X[i])) != Y[i]:
            return False
    return True

def predetermined(T = 1,alpha = 1):
    X,Y = readData()
    X = np.array(X)
    sum = 0
    for exper in xrange(T):
        cnt = 0
        isHalt = False
        w = (np.array([0.0,0.0,0.0,0.0,0.0]))
        random.seed(exper+1)
        CYC = random.sample(xrange(len(X)),len(X))
        #print CYC
        while not isHalt:
            isHalt = False
            for i in CYC:
                if getSign(w.dot(X[i])) != Y[i]:
                    w += 0.5*Y[i]*X[i]
                    isHalt = ISHALT(w, X, Y)
                    cnt+=1
                    if isHalt:
                        break
        sum += cnt
    print sum/T

predetermined(2000, 0.5) # alpha is the step size
