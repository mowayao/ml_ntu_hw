import numpy as np

eps = 1e-8
X = []
Y = []



def getSign(x):
    if x > eps:
        return 1
    else:
        return -1

def readData():
    File = open("D:\\hw1_15_train.dat.txt")
    for line in File.readlines():
        a = map(float,line.split())
        a.insert(-1,1)
        Y.append(getSign(a[-1]))
        X.append(np.array(a[:-1]))

def ISHALT(w,X,Y):
    for i in xrange(len(X)):
        if getSign(w.dot(X[i])) != Y[i]:
            return False
    return True



readData()
X = np.array(X)
isHalt = False
w = (np.array([0.0,0.0,0.0,0.0,0.0]))
cnt = 0
isHalt = False
while not isHalt:
    isHalt = False
    for i in xrange(len(X)):
        if getSign(w.dot(X[i])) != Y[i]:
            w += Y[i]*X[i]
            isHalt = ISHALT(w, X, Y)
            cnt+=1
            if isHalt:
                break
print cnt