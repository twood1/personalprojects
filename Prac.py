import numpy as np

#I broke this some time back. Doesn't work anymore due to some small indexing logic errors
#but it should be very easily fixable

class NeuralNetwork():

    def __init__(self, inputs, outs, numHL, sizeHL):
        self.inputLayerSize = 2
        self.outputLayerSize = 2
        self.inputs = inputs
        self.expOuts = outs
        self.numHL = numHL
        self.hiddenLayerSize = sizeHL

        #self.bias = [.35,.60]
        #self.wArr = [np.matrix([[.15,.25],[.20,.30]]),np.matrix([[.40,.50],[.45,.55]])]


        self.bias = np.random.rand(self.numHL+1)


        if(numHL != 0):
            self.wArr = [   np.matrix(np.random.randn(self.inputLayerSize, self.hiddenLayerSize)), \
                            np.matrix(np.random.randn(self.hiddenLayerSize,self.outputLayerSize))]
        else:
            self.wArr = [np.matrix(np.random.randn(self.inputLayerSize, self.outputLayerSize))]


        for i in range(self.numHL-1):
            self.wArr.insert(1, np.matrix(np.random.randn(self.hiddenLayerSize, self.hiddenLayerSize)))


        self.output = []
        self.innerLayers = []

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoidPrime(self, z):
        return z * (1-z)

    def stdErr(self, target, out):
        return (1/2) * ((target-out)**2)

    def totalErr(self):
        retval = 0
        for i in range(self.output.__len__()):
            for j in range(self.output[i].__len__()):
                retval += self.stdErr(self.expOuts[j], self.output[j])
        return retval

    def delta(self, out, target):
        return -(target - out) * out * (1 - out)

    def forward(self, idx):
        newInner = []
        f = np.vectorize(self.sigmoid)

        test1 = self.wArr[0].T
        test2 = np.matrix(self.inputs[idx]).T
        test3 = np.dot(test1,test2)

        h1 = np.dot(self.wArr[0].T,np.matrix(self.inputs[idx]).T) + self.bias[0]
        h1 = f(h1)
        newInner.append(h1)

        currIns = h1
        for i in range(self.numHL-1):
            tmp = f(np.dot(self.wArr[i+1].T, currIns) + self.bias[i+1])
            newInner.append(tmp)
            currIns = tmp

        self.innerLayers = newInner

        if (self.numHL != 0):
            self.output = np.asarray(f(np.dot(self.wArr[self.numHL].T, currIns) + self.bias[self.numHL]))
        else:
            self.output = np.asarray(currIns)
        return

    def forwardTest(self, testInputs):
        tmp = np.dot(self.wArr[0].T, np.matrix(testInputs).T) + self.bias[0]
        f = np.vectorize(self.sigmoid)
        tmp = f(tmp)

        if(self.numHL != 0):
            currIns = tmp
            for i in range(self.numHL-1):
                tmp = f(np.dot(self.wArr[i+1].T, currIns) + self.bias[i+1])
                currIns = tmp

            output = f(np.dot(self.wArr[self.numHL].T, currIns) + self.bias[self.numHL])

            return output
        else:
            return tmp

    def train(self, learnRate):
        for i in range(self.inputs.__len__()):
            self.forward(i)
            out2 = self.output
            in2 = self.inputs[i]
            expOuts2 = self.expOuts[i]
            deltaVec = []
            wAdjustments = []
            for j in range(out2.__len__()):
                deltaVec.append(self.delta(out2[j], expOuts2[j]))

            deltaVec = np.matrix(deltaVec)

            #decreasing for loop from inner layers-1 to 0 inclusive. hideous syntax
            if (self.numHL != 0):
                for k in range(self.innerLayers.__len__()-1, -1,-1):

                    wAdjustments.insert(0, (learnRate * np.dot(deltaVec, np.matrix(self.innerLayers[k]).T)).T)

                    deltaVec = np.dot(np.matrix(self.wArr[k+1]), deltaVec)


                    for m in range(0, deltaVec.__len__()):
                        deltaVec[m] = deltaVec[m] * self.sigmoidPrime(self.innerLayers[k][m])

            wAdjustments.insert(0, (learnRate * np.dot(deltaVec, np.matrix(in2))).T)

            for i in range(wAdjustments.__len__()):
                self.wArr[i] = self.wArr[i] - wAdjustments[i]
'''
if __name__ == "__main__":
    # [.03, .02], [.05, .03], [.08, .07]] \
    # [.09, .06], [.15, .09], [.24, .21]], \

    NN = NeuralNetwork([[.02,.02],[.05,10],[.30,.11], [.03, .05],[.21,.21],[.47,.12],[.02,.03],[.03,.03],[.04,.08],\
                        [.03,.02],[.07,.11],[.11,.16]], \
                       [[.04],[.15],[.41],[.08],[.42],[.69],[.05],[.06],[.12],[.05],[.18],[.27]], 2, 10)
    NN.train(.5)

    for i in range(500):
        NN.train(.5)

    for i in range(6000):
        NN.train(.5)

    print("____________________")
    print("Test trained input .05+.10: ")
    print(NN.forwardTest([.05, .10]))
    print("Test trained input .30+.11: ")
    print(NN.forwardTest([.30, .11]))
    print("Test trained input .03+.05: ")
    print(NN.forwardTest([.03, .05]))
    print("Test trained input .21+.21: ")
    print(NN.forwardTest([.21,.21]))
    print("Test trained input .47+.12: ")
    print(NN.forwardTest([.47,.12]))
    print("Test trained input .02+.02: ")
    print(NN.forwardTest([.02, .02]))
    print("Test trained input .02+.03: ")
    print(NN.forwardTest([.02, .03]))
    print("Test trained input .03+.03: ")
    print(NN.forwardTest([.03, .03]))
    print("Test trained input .04+.08: ")
    print(NN.forwardTest([.04, .08]))
    print("Test new input .07+.04: ")
    print(NN.forwardTest([.07, .04]))
    print("Test new input .16+.27: ")
    print(NN.forwardTest([.16,.27]))
    print("Test new input .31+.35: ")
    print(NN.forwardTest([.31, .35]))
    print("Test new input .21+.11: ")
    print(NN.forwardTest([.21, .11]))
    print("Test new input .27+.09: ")
    print(NN.forwardTest([.27, .09]))
'''

'''
if __name__ == "__main__":
    inputs = [[1,0],[0,1],[0,0],[1,1]]
    outputs = [[1],[1],[0],[1]]
    NN = NeuralNetwork(inputs,outputs,1,1)

    for i in range(5000):
        NN.train(.5)

    print("Test input 1 0: ")
    print(NN.forwardTest([1, 0]))
    print("Test input 1 1: ")
    print(NN.forwardTest([1, 1]))
    print("Test input 0 1: ")
    print(NN.forwardTest([0, 1]))
    print("Test input 0 0: ")
    print(NN.forwardTest([0, 0]))
    print("Squared Error: ")
    se = 0
    for i in range(inputs.__len__()):
        se += NN.stdErr(NN.forwardTest(inputs[i]),outputs[i])
    print(se)

'''
if __name__ == "__main__":
    NN = NeuralNetwork([[1,0],[0,0],[0,1],[1,1]],[[1],[0],[1],[0]],1,1)

    for i in range(10):
        NN.train(.5)

    print("Input .05 .10: ")
    print(NN.forwardTest([.05,.10]))