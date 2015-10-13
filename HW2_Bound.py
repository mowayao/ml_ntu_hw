__author__ = 'mowayao'
from math import log,sqrt
from random import uniform,seed
def mH(N,dvc):
    return N**dvc
class Bound:
    def __init__(self,N,dvc,confidence):
        self.N = N
        self.dvc = dvc
        self.confidence = confidence
    def VCbound(self):
        return sqrt(8.0/self.N*log(4*mH(2*self.N,self.dvc)/self.confidence))
    def RademacherPenaltyBound(self):
        return sqrt(2.0*log(2*self.N*mH(self.N,self.dvc))/self.N)+sqrt(2.0/self.N*log(1.0/self.confidence))+1.0/self.N
    def ParrondoandVandenBroek(self):
        return (1+sqrt(1+self.N*log(6*mH(2*self.N,self.dvc)/self.confidence)))/self.N
    def Devroye(self):
        return (2+sqrt(4+(2*self.N-4)*(log(4/self.confidence)+2*self.dvc*log(self.N))))/(2*self.N-4)

    def VariantVCbound(self):
        return sqrt(16.0/self.N*log(2*mH(self.N,self.dvc)/sqrt(self.confidence)))



test = Bound(10000,50,0.05)
print test.VCbound()
print test.RademacherPenaltyBound()
print test.VariantVCbound()
print test.ParrondoandVandenBroek()
print test.Devroye()
