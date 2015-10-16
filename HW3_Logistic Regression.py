__author__ = 'mowayao'
import numpy as np
from math import exp
def sign(x):
    if x >= 0:return 1
    else:return -1
def sigmoid(x):
    return 1.0/(1+exp(-x))
class LogisticRegression:
    def __init__(self,Lrate,T,opts):  #Lrate:learning rate
        self.Lrate = Lrate
        self.T = T
        self.opts = opts
        self.TrainX,self.TrainY = self.readData("E:\\hw3_train.dat")
        self.TestX,self.TestY = self.readData("E:\\hw3_test.dat")
    def readData(self,filename):
        F = open(filename)
        X = []
        Y = []
        for line in F.readlines():
            data = map(float,line.split())
            X.append(data[:-1])
            Y.append(data[-1])
        return np.mat(X),np.array(Y).transpose()
    def predict(self,X,w):
        return np.array(X*w)
    def getEinGradient(self,w,nSamples,nFeatures):
        gradient = np.zeros((nFeatures,1))
        Y = self.predict(self.TrainX,w)
        #print Y.shape
        for i in xrange(nSamples):
            py = Y[i]
            x = self.TrainX[i,:]
            y = self.TrainY[i]
            gradient += sigmoid(-1.0*y*py)*(y*x.transpose())
        return gradient/nSamples
    def SGD(self):
        nSamples,nFeature = self.TrainX.shape
        w = np.zeros((nFeature,1))
        for i in range(self.T):
            x = self.TrainX[i%nSamples,:]
            y = self.TrainY[i%nSamples]
            py = sigmoid(x*w)
            w += self.Lrate*sigmoid(-1.0*y*py)*(y*x.transpose())
        return w

    def train(self):
        nSamples,nFeature = self.TrainX.shape
        w = np.zeros((nFeature,1))
        for i in range(self.T):
            w += self.Lrate*self.getEinGradient(w,nSamples,nFeature)
        return w

    def getEout(self,w):
        cnt = 0
        nSamples,nFeature = self.TestX.shape
        Y = self.predict(self.TestX,w)
        for i in xrange(nSamples):
            x = self.TestX[i,:]
            py = Y[i]
            y = self.TestY[i]
            if y != sign(sigmoid(py)-0.5):
                cnt += 1
        print cnt*1.0/nSamples
    def solve(self):
        if self.opts=="SGD":
            w = self.SGD()
        elif self.opts=="Normal":
            w = self.train()
        self.getEout(w)

test1 = LogisticRegression(0.001,2000,"SGD")
test1.solve()
