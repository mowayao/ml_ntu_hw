__author__ = 'mowayao'
def sign(x):
    if x>=0:return 1
    else:return -1
from random import uniform,seed
class DecisionStump:
    def __init__(self,l,r,p,N):
        self.l = l
        self.r = r
        self.p = p
        self.N = N
        self.data = []

    def generateData(self,r):
        seed(r+1)
        for i in xrange(self.N):

            xi = uniform(self.l,self.r)
            if xi >= 0:yi = 1
            else:yi = -1
            p = uniform(0,1)
            if p <=self.p:
                yi = -yi
            self.data.append((xi,yi))
        self.data = sorted(self.data)

    def solve(self):
        Ein = Eout = 0.0
        for i in xrange(5000):
            self.generateData(i)
            th = [(self.data[t-1][0]+self.data[t][0])/2 for t in xrange(1,self.N)]
            th.append(-1)
            th.append(1)
            bestT = -2
            flag = 0
            bestS = 1e9
            for the in th:
                s1 = s2 = 0.0
                for j in xrange(self.N):
                    hj1 = sign(self.data[j][0]-the)
                    if hj1 != self.data[j][1]:
                        s1 += 1
                    hj2 =  -sign(self.data[j][0]-the)
                    if hj2 != self.data[j][1]:
                        s2 += 1
                s1 /= self.N
                s2 /= self.N
                if(bestS > s1):
                    bestS = s1
                    bestT = the
                    flag = 1
                if(bestS > s2):
                    bestS = s2
                    bestT = the
                    flag = -1
            Ein += bestS
            Eout += (0.5+0.3*flag*(1-abs(bestT)))/2
        print Ein/5000,Eout/5000

test = DecisionStump(-1,1,0.2,20)

test.solve()
