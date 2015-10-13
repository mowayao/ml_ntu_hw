__author__ = 'mowayao'

def sign(x):
    if x>=0:return 1
    else:return -1

class DecisionStump: #for multi-dimensional data
    def __init__(self):
        self.data = []
    def readData(self):
        File = open("D:\\hw2_train.dat")
        for line in File.readlines():
            d = map(float,line.split())
            self.data.append(d)
        self.dim = len(self.data[0])-1
    def Train(self):
        self.readData()
        bestEin = 1e9
        bestTh = -1
        bestDim = -1
        flag = 0
        for i in xrange(self.dim):
            xy = []
            for j in  xrange(0,len(self.data)):
                xy.append((self.data[j][i],self.data[j][-1]))
            xy = sorted(xy)
            th = [(xy[j][0]+xy[j-1][0])/2 for j in xrange(1,len(xy))]
            th.append(1e9)
            th.append(-1e9)
            for the in th:
                Ein1 = Ein2 = 0.0
                for j in xrange(len(xy)):
                    if sign(xy[j][0]-the) != int(xy[j][1]):
                        Ein1 += 1
                    if -sign(xy[j][0]-the) != int(xy[j][1]):
                        Ein2 += 1
                Ein2 = Ein2/len(xy)
                Ein1 = Ein1/len(xy)
                if Ein1 < bestEin:
                    bestEin = Ein1
                    bestTh = the
                    bestDim = i
                    flag = 1
                if Ein2 < bestEin:
                    bestEin = Ein2
                    bestTh = the
                    bestDim = i
                    flag = -1
        print bestEin
        return bestTh,bestDim,flag

    def test(self):
        bestTh,bestDim,flag = self.Train()
        File = open("D:\\hw2_test.dat")
        testData = []
        cnt = 0
        Eout = 0.0
        for line in File.readlines():
            d = map(float,line.split())
            #print d
            cnt += 1
            if flag*sign(d[bestDim]-bestTh) != int(d[-1]):
                Eout += 1
        print Eout/cnt

test = DecisionStump()
test.test()

