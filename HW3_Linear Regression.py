__author__ = 'mowayao'
from random import uniform,seed
import numpy as np
from numpy.linalg import inv
from math import exp
def sign(x):
    if x >= 0:return 1
    else:return -1
class LinearRegression():
    def __init__(self,trainingSize,minX,maxX):
        self.trainingSize = trainingSize
        self.minX = minX
        self.maxX = maxX

    def generateData(self):
        X = []
        Y = []
        for i in xrange(self.trainingSize):
            x0 = uniform(self.minX,self.maxX)
            x1 = uniform(self.minX,self.maxX)
            fv = self.f((x0,x1))
            p = uniform(0,1)
            if p <= 0.1:
                fv = -fv
            X.append([1,x0,x1])
            Y.append(fv)
        return X,Y
    def training(self,tX,tY):
        #self.trainX,self.trainY= self.generateData()
        xT = np.transpose(np.mat(tX))
        x = np.mat(tX)
        y = np.array(tY)
        w = np.dot(inv(xT*x)*xT,y)
        return w

    def transform(self,x):
        X = []
        for i in xrange(len(x)):
            t = [x[i][0],x[i][1],x[i][2],x[i][1]*x[i][2],x[i][1]**2,x[i][2]**2]
            X.append(t)
        return X
    def getErr(self,y1,y2):
        cnt = 0
        for i in xrange(len(y1)):
            if sign(y1[i]) != y2[i]:
                cnt+=1
        return cnt
    def getEin(self):
        ret = 0
        for i in xrange(1000):
            seed(i)
            trainX,trainY = self.generateData()
            w = self.training(trainX,trainY).transpose()
            yt = np.dot(np.mat(trainX),w)
            cnt = self.getErr(yt,trainY)
            ret += cnt*1.0/self.trainingSize
        print ret/1000
    def getEout(self):
        ret = 0
        for i in xrange(1000):
            seed(i*2)
            tX,tY = self.generateData()
            xt = self.transform(tX)
            w = self.training(xt,tY).transpose()
            seed(i*2+1)
            testX,testY = self.generateData()
            testX = self.transform(testX)
            cnt = self.getErr(np.dot(np.mat(testX),w),testY)
            ret += cnt*1.0/1000
        print ret/1000
    def solve(self):
        self.getEin()
        self.getEout()
    def f(self,x):
        return sign(x[0]**2+x[1]**2-0.6)

#test = LinearRegression(1000,-1,1)
#test.solve()


class SolutionToNewtonDirection:
    def __init__(self,u,v):
        self.u = u
        self.v = v
    def E(self,u,v):
        return exp(u)+exp(2*v)+exp(u*v)+u**2-2*u*v+2*v**2-3*u-2*v
    def ComputeGradient(self,u,v):
        bu = exp(u)+v*exp(u*v)+2*u-2*v-3
        bv = 2*exp(2*v)+u*exp(u*v)-2*u+4*v-2
        buv = exp(u*v)+u*v*exp(u*v)-2
        bvv = 4*exp(2*v)+u*u*exp(u*v)+4
        buu = exp(u)+v*v*exp(u*v)+2
        h = [[buu,buv],[buv,bvv]]
        g = [bu,bv]
        return np.array(g),np.array(h)
    def solve(self):
        a = b = 0
        for i in xrange(5):
            g,H = self.ComputeGradient(self.u,self.v)
            g = np.transpose(g)
            gradient = np.dot(np.linalg.inv(H),g)
            #gradient = *g
            tg,th = self.ComputeGradient(a,b)
            a -= tg[0]*0.01
            b -= tg[1]*0.01
            self.u -= gradient[0]
            self.v -= gradient[1]
        print self.E(self.u,self.v)
        print self.E(a,b)
test1 = SolutionToNewtonDirection(0,0)
test1.solve()
#H = np.mat([[3,-1],[-1,8]])


