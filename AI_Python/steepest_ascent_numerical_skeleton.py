import random
import math

# 전역변수 두개
DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations 


def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm

    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = steepestAscent(p) ## !!주변에서 젤 좋은걸로 이동하는 알고리즘

    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()

    # Report results
    displayResult(solution, minimum)

## line = f,readline().rstrip() 이렇게 한줄씩 할 수도 있다.
def createProblem(): ###
    # proName = input("What kinda problem do you want to solve?()")
    proName = "Convex"
    file = open("./Search Tool Sample Problems/" + proName + ".txt",'r')
    content = file.read()
    tp = content.split('\n') ## ?
    print('tp[0]',tp[0])
    expression = tp[0]
    varName = []
    low = []
    up = []
    domain = []
    for i in range(1,len(tp)-1):             ### 1~끝 : 
        ## [varName, low, up]
        # 1. content[i] ','단위로 찢기
        temp = tp[i].split(',')    ## [0] : varName, [1] : low, [2]: up
        print("temp",temp)
        varName.append(temp[0])
        low.append(eval(temp[1]))
        up.append(eval(temp[2]))
        ## templist = [varName, low, up] 일케 구성됨.
    domain.append(varName)
    domain.append(low)
    domain.append(up)
    print("expression",expression)
    print("domain",domain)
    file.close()
    return expression, domain


def steepestAscent(p):
    current = randomInit(p)
    valueC = evaluate(current,p)
    while True:
        neighbors = mutants(current,p)
        # 각각의 neighbor에 대해 함수 값 계산 => 더 좋은거 있으면 이동
        best, bestValue = bestOf(neighbors,p)
            
    # tempInit = randomInit(p)
    # for i in range(0,len(p[1][0])):
    #     p[1][0][i] = tempInit[i]
    # funVal = exec(p[0])         ### 초기 값에 대한 함숫값 계산
    # Random한 초기값을 생성
    # for i in range(0,len(temp[1][0])):
    # for i in temp[1][0]:
    #     i = random.randrange(temp[1][1],temp[1][2])
    # 초기값에 대한 함수값을 계산
    # funVal = exec(temp[0])
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
        # mutant를 생성
        ## w
        # mutant 중 가장 좋은 solution을 선택
        
        # best solution 업데이트
        
    # Best solution과 그때의 Cost를 반환
    return current, valueC


def randomInit(p):
    init = []
    for i in range(0,len(p[1][0])):
        init.append(random.uniform(p[1][1][i],p[1][2][i]))
    return init

def evaluate(current, p):   ## 함수값 계산
    global NumEval
    NumEval += 1
    domain = p[1]
    varName = domain[0]
    for i in range(0,len(varName)):
        exec(varName[i] + '=' + str(current[i]))
    valueC = eval(p[0])
    print("vC",valueC)
    return valueC

#


def mutants(current, p):## current : 변수들 전부 다 (이 경우 5개)
    # Return a set of successors
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환
    neighbors = []
    for i in range(len(current)):
        neighbors.append(mutate(current,i,-DELTA,p))
        neighbors.append(mutate(current,i,DELTA,p))
        # [+del,-del]
    return neighbors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    neighbor = current[:]
    # low,up = domain[1],domain[2]
    # if low[i] <= neighbor[i] + d <= up[i]: <= 일케도 가능.
    if(neighbor[i]+d>=p[1][1][i] and neighbor[i]+d<=p[1][2][i]):
        neighbor[i] += d
    elif(neighbor[i]+d>=p[1][2][i]):
        neighbor[i]=p[1][2][i]
    elif(neighbor[i]+d<p[1][1][i]):
        neighbor[i]=p[1][1][i]              ### 무한루프에 대한 걱정 꼭 하기
    print("neighbor",neighbor)
    return neighbor # 값이 5개 들어있는 리스트 (current와 동일 형태)

def bestOf(neighbors, p):
    # 1. 가장 처음 sample을 best라 가정.
    # 2. 두 번째 부터 계속 비교하면서 더 좋은게 찾아지면 best로 저장해 둔다.
    # 3. 모두 다 비교 끝나면 best 반환
    best = neighbors[0]
    bestValue = evaluate(best,p)
    
    for i in range(1,len(neighbors)):
        newValue = evaluate(neighbors[i],p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
