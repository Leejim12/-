import random
import math


## Numeric : 
## Tsp : 
class Problem:
    def __init__(self):
        self._solution = None   ##약속. class 변수이다.
        self._value = 0
        self._numEval = 0
    ## self : 자기 자신에 대한 참조가 첫번째 argument로 들어가야함.
    def setVariables(self):
        # self._numEval 
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
        self._expression = ""
        self._domain = []
        self._Delta = 0.01
        
    def setVariables(self):
        ## 인풋 -> cP -> exp, domain 업데이트
        proName =  input("What kinda problem do you want to solve?")
        file = open("./Search Tool Sample Problems/" + proName + ".txt",'r')
        content = file.read()
        tp = content.split('\n') ## ?
        self._expression = tp[0]
        varName = []
        low = []
        up = []
        domain = []

        for i in range(1,len(tp)-1):
            temp = tp[i].split(',')
            varName.append(temp[0])
            low.append(eval(temp[1]))
            up.append(eval(temp[2]))
        domain.append(varName)
        domain.append(low)
        domain.append(up)
        self._domain.append(domain)
        file.close()


    
    def getDelta(self):
        return self._Delta
    
    def randomInit(self): # Return a random initial point as a list
        init = []
        p = self._domain
        for i in range(0,len(p[1])):
            init.append(random.uniform(p[1][i],p[2][i]))
        return init
    
    def evaluate(self, current):
        
        p = self._domain
        varName = self._domain[0]
        self._numEval += 1

        for i in range(0,len(varName)):
            exec(varName[i] + '=' + str(current[i]))
        valueC = eval(self._expression)
        return valueC
    
    def mutants(self, current):
        p = self._domain
        neighbors = []
        for i in range(len(current)):
            neighbors.append(self.mutate(current,i,-self._Delta))
            neighbors.append(self.mutate(current,i,self._Delta))
            # [+del,-del]
        return neighbors
    
    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        p = self._domain
        # low,up = domain[1],domain[2]
        # if low[i] <= neighbor[i] + d <= up[i]: <= 일케도 가능.
        if(neighbor[i]+d>=p[1][i] and neighbor[i]+d<=p[2][i]):
            neighbor[i] += d
        elif(neighbor[i]+d>=p[2][i]):
            neighbor[i]=p[2][i]
        elif(neighbor[i]+d<p[1][i]):
            neighbor[i]=p[1][i]
        print("neighbor",neighbor)
        return neighbor
    
    # def randomMutant(self, current):
        
    
    def describe(self):
        p = self._domain
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
    
    
Numeric()