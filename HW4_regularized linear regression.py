__author__ = 'mowayao'
import numpy as np
from numpy.linalg import inv

def getSign(x):
    if x <= 0:
        return -1
    else:
        return 1
def KFold(nSamples,nFold):
    foldSize = nSamples/nFold
    for i in xrange(nFold):
        indices = ~np.ones((nSamples,),dtype=np.bool)
        sta = i*foldSize
        ed = sta + foldSize
        indices[sta:ed] = True
        yield indices

class reguLinearRegression:
    def __init__(self, le,flag=False,cv=False):
        train = np.genfromtxt("hw4_train.dat")
        test = np.genfromtxt("hw4_test.dat")
        self.Xtest, self.Ytest = np.hstack((np.ones((test.shape[0],1)),test[:,:-1])),test[:,-1]
        self.le = le
        if not flag:
            self.Xtrain, self.Ytrain = np.hstack((np.ones((train.shape[0],1)),train[:,:-1])),train[:,-1]
        else:
            curX = np.hstack((np.ones((train.shape[0],1)),train[:,:-1]))
            self.Xtrain,self.Ytrain = curX[:120,:],train[:120,-1]
            self.Xval,self.Yval = curX[120:,:],train[120:,-1]
        if not cv:
            self.w = self.Train(self.Xtrain, self.Ytrain)

    def getEcv(self):
        Ecv = 0
        for ind in KFold(self.Xtrain.shape[0],5):
            Xtr,self.Xval= self.Xtrain[~ind],self.Xtrain[ind]
            Ytr,self.Yval = self.Ytrain[~ind],self.Ytrain[ind]
            self.w = self.Train(Xtr,Ytr)
            Ecv += self.getEval()
        return Ecv/5
    def Train(self,X,Y):
        X = np.mat(X)
        XTX = X.transpose()*X
        nFeatrues, nFeatrues = XTX.shape
        lambdaI = self.le * np.identity(nFeatrues)
        tx = (XTX+lambdaI).getI()*X.transpose()
        ty = np.mat(Y).transpose()
        theta=np.squeeze(np.asarray((tx*ty).transpose()))
        return theta
    def getErr(self,pY,Y,nSamples):
        wr = 0
        for i in xrange(nSamples):
            if getSign(pY[i]) != Y[i]:
                wr += 1
        return wr
    def getEin(self):
        nSamples, nFeatures = self.Xtrain.shape
        Y = np.dot(np.mat(self.Xtrain),self.w.transpose()).transpose()
        wro = self.getErr(Y,self.Ytrain,nSamples)
        return float(wro)/nSamples
    def getEval(self):
        nSamples, nFeatures = self.Xval.shape
        Y = np.dot(np.mat(self.Xval),self.w.transpose()).transpose()
        wro = self.getErr(Y,self.Yval,nSamples)
        return float(wro)/nSamples
    def getEout(self):
        nSamples, nFeatures = self.Xtest.shape
        Y = np.dot(np.mat(self.Xtest),self.w.transpose()).transpose()
        wro = self.getErr(Y,self.Ytest,nSamples)
        return float(wro)/nSamples
# 13
print "Q13"

test = reguLinearRegression(10)
print test.getEin(),test.getEout()
print
print "Q14"
#14

lembdas = [10** i for i in xrange(-10,3)]
print lembdas
ret = -1
minEin = 1e8
for lembda in lembdas:
    test = reguLinearRegression(lembda)
    tmp = test.getEin()
    if(tmp <= minEin):
        minEin = tmp
        ret = lembda

print ret,minEin
print
#15
print "Q15"

ret = -1
minEout = 1e8
for lembda in lembdas:
    test = reguLinearRegression(lembda)
    tmp = test.getEout()
    if(tmp <= minEout):
        minEout = tmp
        ret = lembda
print ret,minEout
print
#16
print "Q16"


ret = -1
minEin = 1e8
Eout = Eval= -1
for lembda in lembdas:
    test = reguLinearRegression(lembda,True)
    tmp = test.getEin()
    if(tmp <= minEin):
        minEin = tmp
        ret = lembda
        Eval = test.getEval()
        Eout = test.getEout()
print ret,minEin,Eval,Eout
print

print "Q17 and Q18"
#17 and 18
ret = -1
minEval = 1e8
Eout = Ein= -1
for lembda in lembdas:
    test = reguLinearRegression(lembda,True)
    tmp = test.getEval()
    if(tmp <= minEval):
        minEval = tmp
        Eout = test.getEout()
        Ein = test.getEin()
        ret = lembda
print ret,Ein,minEval,Eout

test = reguLinearRegression(ret,False)
print test.getEin(),test.getEout()
print

print "Q19 and Q20"
ret = -1
minEcv = 1e8
Eout = Ein= -1
for lembda in lembdas:
    test = reguLinearRegression(lembda,cv=True)
    tmp = test.getEcv()
    if(tmp <= minEcv):
        minEcv = tmp
        ret = lembda
print ret,minEcv

test = reguLinearRegression(ret)
print test.getEin(),test.getEout()


