import random
import math


class Problem:
    def __init__(self):
        self._solution = None
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self._expression = ''
        self._domain = []
        self._delta = 0.01

    def setVariables(self):
        f = open('Convex.txt', 'r')
        self._expression = f.readline().rstrip()

        varNames = []
        low = []
        up = []

        line = f.readline().rstrip()
        while line != '':
            d = line.split(',')
            varNames.append(d[0])
            low.append(eval(d[1]))
            up.append(eval(d[2]))

            line = f.readline().rstrip()

        self._domain = [varNames, low, up]

    def getDelta(self):
        return self._delta

    def randomInit(self): # Return a random initial point as a list
        low, up = self._domain[1], self._domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.uniform(low[i], up[i]))
        return init

    def evaluate(self, current):
        self._numEval += 1
        varName = self._domain[0] # 여기에서 변수 명을 참조

        for i in range(len(varName)):
            cmd = varName[i] + '=' + str(current[i])
            exec(cmd)

        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []

        for i in range(len(current)):
            m = self.mutate(current, i, self._delta)
            neighbors.append(m)
            m = self.mutate(current, i, -self._delta)
            neighbors.append(m)
        
        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]

        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d

        return neighbor

    # def randomMutant(self, current):

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(self._expression)   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple
    
    
class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._distanceTable = []
        
    def setVariables(self):
        fileName = './TSP/tsp30.txt'
        infile = open(fileName,'r')
        line = infile.read()
        temp = line.split("\n")
        infile.close()
        self._numCities = int(temp[0])
        temp2 = temp[1:-1]
        for i in temp2:
            i = i[1:-1]
            self._locations.append(i.split(','))
        for i in range(len(self._locations)):
            for j in range(len(self._locations[0])):
                self._locations[i][j] = int(self._locations[i][j])
        self._distanceTable = self.calcDistanceTable(self._numCities, self._locations)
    
    def calcDistanceTable(self):    # o
        table = []
        for i in range(0,self._numCities):
            row = []
            for j in range(0,self._numCities):
                d = round(math.sqrt((self._locations[i][0]-self._locations[j][0])**2+(self._locations[i][1]-self._locations[j][1])**2),1)
                row.append(d)
            table.append(row)
        self._distanceTable =  table
        return self._distanceTable
    
    
    def randomInit(self):
        init = list(range(self._numCities))
        # for i in range(0,p[0]):##체크
        #     init.append(i)
        random.shuffle(init)
        return init
    
    def evaluate(self,current): # o
        ## current : 도시 방문 인덱스 순서
        self._numEval+= 1
        cost = 0
        for i in range(0,len(current)-1):
            cost += self._distanceTable[current[i]][current[i+1]]
        cost = round(cost,1)
        return cost
    
    def mutants(self,current, p): # Apply inversion
        triedPairs = []
        neighbors = []
        while len(triedPairs)<s:
            i,j = random.randint(0,self._numCities-1),random.randint(0,self._numCities-1) # 숫자 1개
            if i>j:
                i,j = j,i
            if [i,j] not in triedPairs:
                triedPairs.append([i,j])
            else:
                continue
        for i in triedPairs:
            neighbors.append(self.inversion(current,i[0],i[1]))
        return neighbors

    def inversion(self,current, i, j):
        curCopy = current[:]
        temp = curCopy[i:j+1]
        temp.reverse()
        curCopy[i:j+1] = temp
        return curCopy
    
    def bestOf(self,neighbors):   # x
    # neighbots 중 가장 cost가 작은 neighbor 선정
        best = neighbors[0]
        bestValue = self.evaluate(best)
        
        for i in range(1,len(neighbors)):
            newValue = self.evaluate(neighbors[i])
            if newValue < bestValue:
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue
    
    def describeProblem(self,p):
        print()
        n = p[0]
        print("Number of cities:", n)
        print("City locations:")
        locations = p[1]
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")

    def displayResult(self,solution, minimum):
        print()
        print("Best order of visits:")
        self.tenPerRow(solution)       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        print()
        print("Total number of evaluations: {0:,}".format(self._NumEval))

    def tenPerRow(self,solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()
                
    p = Problem
    p.setVariables()
    