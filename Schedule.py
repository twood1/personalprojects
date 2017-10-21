import random
import copy
import sys
import datetime

class ClassMatrix:
    def __init__(self, n):
        self.score = 0
        self.n = n
        self.origin = list(range(1,n+1))
        self.firstHalfL1 = []
        self.firstHalfP1 = []
        self.firstHalfS1 = []
        self.firstHalfL2 = []
        self.firstHalfP2 = []
        self.firstHalfS2 = []
        self.secondHalfL1 = []
        self.secondHalfP1 = []
        self.secondHalfS1 = []
        self.secondHalfL2 = []
        self.secondHalfP2 = []
        self.secondHalfS2 = []

    # 2 randomly generated segments: second half presenter2 and second half scribe2
    def makeSeed(self):
        #generate arrays for first half of semester
        self.firstHalfL1 = list(range(1, self.n / 2 + (self.n % 2 > 0) + 1))
        self.firstHalfP1 = list(range(self.n, self.n / 2 + (self.n % 2 > 0) - 1, -1))
        self.firstHalfS1 = list(range(self.n / 4 + (self.n % 4 > 0), 0, -1))
        i = self.n
        while len(self.firstHalfS1) != len(self.firstHalfP1):
            self.firstHalfS1.append(i)
            i -= 1

        self.firstHalfL2 = list(range(int(self.n / 2 + (self.n % 2 > 0)) + 1, self.n + 1))
        self.firstHalfP2 = list(range(int(self.n / 2 + (self.n % 2 > 0)) - 1, 0, -1))
        tmp = list(set(self.origin)-set(self.firstHalfS1))
        i, j = 0, len(tmp) - 1
        while j >= i:
            if j == i:
                self.firstHalfS2.append(tmp[i])
                break
            self.firstHalfS2.append(tmp[j])
            self.firstHalfS2.append(tmp[i])
            j -= 1
            i += 1

        #set up second half of the semester
        self.secondHalfL1 = list(range(self.n / 2 + (self.n % 2 > 0) + 1, self.n + 1))
        self.secondHalfP1 = list(range(self.n / 2 + (self.n % 2 > 0) - 1, 0, -1))
        self.secondHalfS1 = copy.deepcopy(self.firstHalfS2)
        self.secondHalfL2 = list(range(1, self.n / 2 + (self.n % 2 > 0) + 1))
        self.secondHalfP2 = list(set(self.origin) - set(self.firstHalfP2))
        self.secondHalfS2 = list(set(self.origin) - set(self.firstHalfS2))
        random.shuffle(self.secondHalfP2)
        random.shuffle(self.secondHalfS2)

        if self.n % 2 != 0:
            self.firstHalfS2.append(None)
            self.firstHalfP2.append(None)
            self.firstHalfL2.append(None)
            self.secondHalfL1.append(None)
            self.secondHalfP1.append(None)
            self.secondHalfS1.append(None)

    def makeRandomSeed(self):

        #set first half of semester random arrays
        self.firstHalfL1 = list(range(1, self.n + 1))
        self.firstHalfP1 = list(range(1, self.n + 1))
        self.firstHalfS1 = list(range(1, self.n + 1))
        random.shuffle(self.firstHalfL1)
        random.shuffle(self.firstHalfP1)
        random.shuffle(self.firstHalfS1)
        self.firstHalfL2 = self.firstHalfL1[int(self.n / 2 + (self.n % 2 > 0)):]
        self.firstHalfL1 = self.firstHalfL1[:int(self.n / 2 + (self.n % 2 > 0))]
        self.firstHalfP2 = self.firstHalfP1[int(self.n / 2 + (self.n % 2 > 0)):]
        self.firstHalfP1 = self.firstHalfP1[:int(self.n / 2 + (self.n % 2 > 0))]
        self.firstHalfS2 = self.firstHalfS1[int(self.n / 2 + (self.n % 2 > 0)):]
        self.firstHalfS1 = self.firstHalfS1[:int(self.n / 2 + (self.n % 2 > 0))]

        #set second half of semester random arrays.
        self.secondHalfL1 = list(set(self.origin) - set(self.firstHalfL1))
        self.secondHalfP1 = list(set(self.origin) - set(self.firstHalfP1))
        self.secondHalfS1 = list(set(self.origin) - set(self.firstHalfS1))
        self.secondHalfL2 = list(set(self.origin) - set(self.firstHalfL2))
        self.secondHalfP2 = list(set(self.origin) - set(self.firstHalfP2))
        self.secondHalfS2 = list(set(self.origin) - set(self.firstHalfS2))
        random.shuffle(self.secondHalfL1)
        random.shuffle(self.secondHalfP1)
        random.shuffle(self.secondHalfS1)
        random.shuffle(self.secondHalfL2)
        random.shuffle(self.secondHalfP2)
        random.shuffle(self.secondHalfS2)

        if self.n % 2 != 0:
            self.firstHalfS2.append(None)
            self.firstHalfP2.append(None)
            self.firstHalfL2.append(None)
            self.secondHalfL1.append(None)
            self.secondHalfP1.append(None)
            self.secondHalfS1.append(None)


    def check(self):
        test = [self.firstHalfL1 + self.firstHalfL2, self.firstHalfP1 + self.firstHalfP2, \
                self.firstHalfS1 + self.firstHalfS2, self.secondHalfL1 + self.secondHalfL2, \
                self.secondHalfP1 + self.secondHalfP2, self.secondHalfS1 + self.secondHalfS2]
        for ele in test:
            if len(set(ele)) != len(ele):
                print ("error in: " + str(ele))
            if list(set(self.origin) - set(ele)):
                print ("error in: " + str(ele))

    def prettyprint(self):
        test = [self.firstHalfL1 + self.secondHalfL1, self.firstHalfP1 + self.secondHalfP1, \
                self.firstHalfS1 + self.secondHalfS1, self.firstHalfL2 + self.secondHalfL2, \
                self.firstHalfP2 + self.secondHalfP2, self.firstHalfS2 + self.secondHalfS2]

        filename = str(var) + "_" + str(datetime.datetime.now().microsecond)+str(datetime.datetime.now().second) \
                    +"_score"+str(self.score)+".csv"
        myfile = open(filename, 'w+')
        lines = []
        lines.append("-,G1:Presenter,G1:Leader,G1:Scribe,G2:Presenter,G2:Leader,G2:Scribe\n")
        for i in range(0,len(test[0])):
            line = "Day"+str(i+1)+","
            for arr in test:
                line += str(arr[i])+","
            lines.append(line+"\n")
        myfile.writelines(lines)
        myfile.write("Score,"+str(self.score)+"\n")
        myfile.close()

        for ele in test:
            print ele
        print("score: "+str(self.score))

    # Computes score variable, the higher the score the lower the fitness (score of 0 = infinite fitness), but
    # fitness is not computed directly it's just abstract here. Only thing computed is score.
    def fitness(self,sd,btb,sg,printToggle):
        self.score = 0
        L1 = self.firstHalfL1 + self.secondHalfL1
        P1 = self.firstHalfP1 + self.secondHalfP1
        S1 = self.firstHalfS1 + self.secondHalfS1
        L2 = self.firstHalfL2 + self.secondHalfL2
        P2 = self.firstHalfP2 + self.secondHalfP2
        S2 = self.firstHalfS2 + self.secondHalfS2
        # add 100 score for every occurrence of the same individual on the same day
        # add 50 score for each time someone presents or leads on back to back days
        i = 0
        stop = self.n + (self.n % 2 > 0)
        partners = {}
        while i < stop:
            day = [L1[i],P1[i],S1[i],L2[i],P2[i],S2[i]]
            day = list(filter(lambda a: a != None, day))
            val = 0
            if L1[i] == None or L2[i] == None:
                val = 3-len(set(day))
            else:
                val = 6-len(set(day))
            self.score += val*sd
            if printToggle and val:
                print("Has same day")

            val = 0
            # lol, not in the mood to do this cleverly
            if i != 0:
                if L1[i] == L1[i-1]:
                    val += 1
                if L1[i] == L2[i-1]:
                    val += 1
                if L1[i] == P1[i-1]:
                    val += 1
                if L1[i] == P2[i-1]:
                    val += 1
                if L2[i] == L1[i-1]:
                    val += 1
                if L2[i] == L2[i-1]:
                    val += 1
                if L2[i] == P1[i-1]:
                    val += 1
                if L2[i] == P2[i-1]:
                    val += 1
                if P1[i] == L1[i-1]:
                    val += 1
                if P1[i] == L2[i-1]:
                    val += 1
                if P1[i] == P1[i-1]:
                    val += 1
                if P1[i] == P2[i-1]:
                    val += 1
                if P2[i] == L1[i-1]:
                    val += 1
                if P2[i] == L2[i-1]:
                    val += 1
                if P2[i] == P1[i-1]:
                    val += 1
                if P2[i] == P2[i-1]:
                    val += 1
            self.score += btb*val
            if printToggle and val:
                print("Has back to back")

            #add group to partners hash for later scoring
            if L1[i] not in partners:
                if L1[i]:
                    partners[L1[i]] = [P1[i],S1[i]]
            else:
                partners[L1[i]].append(P1[i])
                partners[L1[i]].append(S1[i])

            if P1[i] not in partners:
                if P1[i]:
                    partners[P1[i]] = [L1[i],S1[i]]
            else:
                partners[P1[i]].append(L1[i])
                partners[P1[i]].append(S1[i])

            if S1[i] not in partners:
                if S1[i]:
                    partners[S1[i]] = [L1[i],P1[i]]
            else:
                partners[S1[i]].append(L1[i])
                partners[S1[i]].append(P1[i])

            if L2[i] not in partners:
                if L2[i]:
                    partners[L2[i]] = [P2[i],S2[i]]
            else:
                partners[L2[i]].append(P2[i])
                partners[L2[i]].append(S2[i])

            if P2[i] not in partners:
                if P2[i]:
                    partners[P2[i]] = [L2[i],S2[i]]
            else:
                partners[P2[i]].append(L2[i])
                partners[P2[i]].append(S2[i])

            if S2[i] not in partners:
                if S2[i]:
                    partners[S2[i]] = [L2[i],P2[i]]
            else:
                partners[S2[i]].append(L2[i])
                partners[S2[i]].append(P2[i])

            i += 1

        #for ele in partners:
        #    print str(ele) +" : " +str(partners[ele])
        #    if len(partners[ele]) != 12:
        #       print "not hashed correct"

        # Adds to score the penalty for same group, times the number of times that person is paired with the same person
        for ele in partners:
            val = 12-len(set(partners[ele]))
            self.score += sg*val

    #mutates appropriate positions in the matrix, randomly.
    def mutate(self):
        v1 = random.randint(1,12)
        arr1,arr2 = [],[]
        if v1 == 1 or v1 == 4:
            arr1 = self.firstHalfL1
            arr2 = self.firstHalfL2
        if v1 == 2 or v1 == 5:
            arr1 = self.firstHalfP1
            arr2 = self.firstHalfP2
        if v1 == 3 or v1 == 6:
            arr1 = self.firstHalfS1
            arr2 = self.firstHalfS2
        if v1 == 7 or v1 == 10:
            arr1 = self.secondHalfL1
            arr2 = self.secondHalfL2
        if v1 == 8 or v1 == 11:
            arr1 = self.secondHalfP1
            arr2 = self.secondHalfP2
        if v1 == 9 or v1 == 12:
            arr1 = self.secondHalfS1
            arr2 = self.secondHalfS2

        pos1,pos2 = random.randint(0,len(arr1)-1), random.randint(0,len(arr2)-1)
        while arr1[pos1] == None:
            pos1 = random.randint(0,len(arr1)-1)
        while arr2[pos2] == None:
            pos2 = random.randint(0,len(arr2)-1)

        tmp = arr1[pos1]
        arr1[pos1] = arr2[pos2]
        arr2[pos2] = tmp

var = input("Enter number of students between 10 and 20: ")
while int(var) < 0 or int(var) > 20 or int(var) < 10:
    var = input("Num. not between 10 and 20. Enter num between 10 and 20: ")

sims = input("Enter number of simulations to run (positive integer, I suggest ~3): ")
while int(sims) < 0:
    sims = input("Enter a positive integer number of simulations: ")

sims = int(sims)
var = int(var)
winners = []

for simulation in range(0,sims):
    print ("simulation : "+str(simulation))
    seed = ClassMatrix(var)
    seed.makeRandomSeed()
    seed.fitness(100, 50, 2, False)
    best = seed

    for j in range(0,50):
        parents = [best]
        genK = []

        for k in range(0,200):
            tmp = copy.deepcopy(best)
            genK.append(tmp)

            idx = random.randint(0,len(parents)-1)
            individual = parents[idx]
            if individual.score < 30:
                i = 15
            elif individual.score < 50:
                i = 12
            elif individual.score < 100:
                i = 10
            elif individual.score < 200:
                i = 8
            elif individual.score < 500:
                i = 5
            elif individual.score < 1000:
                i = 3
            else:
                i = 1

            while i > 0:
                offspring = copy.deepcopy(individual)
                offspring.mutate()
                offspring.fitness(100,50,2,False)
                if offspring.score < best.score:
                    best = offspring
                genK.append(offspring)
                i -= 1

            random.shuffle(genK)
            parents = genK[:100]

    winners.append(best)
    if best.score == 0:
        print("Zero score found. Terminating.")
        break


best = winners[0]
for ele in winners:
    if ele.score < best.score:
        best = ele

best.prettyprint()


#matr2.fitness(100,50,2)