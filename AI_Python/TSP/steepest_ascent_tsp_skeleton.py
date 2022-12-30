import random,math

NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, table)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
def createProblem(): # o
    fileName = 'tsp30.txt'
    infile = open(fileName,'r')
    line = infile.read()
    temp = line.split("\n")
    infile.close()
    numCities = int(temp[0])
    temp2 = temp[1:-1]
    locations = []
    for i in temp2:
        i = i[1:-1]
        locations.append(i.split(','))
    for i in range(len(locations)):
        for j in range(len(locations[0])):
            locations[i][j] = int(locations[i][j])
    
        
        
    
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    # txt 파일 이름을 입력 받아서 open 한다.
    
    # First line is number of cities
    # 첫 번째 줄에는 도시의 수가 기록되어 있음
    

    # 두 번째 줄 부터는 각 도시의 위치 (x, y 좌표) 가 기록되어 있음
    
    # 각 도시 사이의 거리를 미리 계산해 둠 (추후 계산의 편의를 위해)
    table = calcDistanceTable(numCities, locations)

    # 출력 예시
    # numCities: 30 (정수 값)
    # locations: [(8, 31), (54, 97), (50, 50), ...] (List of tuples)
    # table: return value of calcDistanceTable
    
    return numCities, locations, table


def calcDistanceTable(numCities, locations):    # o
    # 도시 사이의 거리를 미리 계산해 두어서 표로 준비
    # 직선 거리는 아래와 같은 수식을 이용해 구한다
    # dist = sqrt((x1-x2)^2 + (y1-y2)^2)
    table = []
    for i in range(0,numCities):
        row = []
        for j in range(0,numCities):
            d = round(math.sqrt((locations[i][0]-locations[j][0])**2+(locations[i][1]-locations[j][1])**2),1)
            row.append(d)
        table.append(row)
    # 출력 예시
    # table: [[0.0, 80.4487, 46.0997, ...], [80.4487, 0.0, 47.1699, ...], ...]
    # 이중 list 이고, table[i][j] 의 값은 i번쨰 도시와 j번째 도시 사이의 직선 거리를 나타냄
    return table # A symmetric matrix of pairwise distances


def steepestAscent(p):  # x
    # 시작 지점으로 Random한 방문 순서를 생성
    current = randomInit(p)
    # 생성한 시작 지점의 방문 비용을 evaluate로 계산
    valueC = evaluate(current,p)

    while True:
        # mutants를 생성함
        neighbors = mutants(current,p)
        # mutants 중 best인 solution을 찾는다
        best,bestValue = bestOf(neighbors,p)
        if valueC < bestValue:
            break
        else:
            current = best
            valueC = bestValue
        # for i in neighbors:
        #     tempDistance = evaluate(i,p)
        #     if tempDistance < cost:
        #         cost = tempDistance
        #         current = i
        # # best가 현재 보다 좋으면 업데이트, 아니면 while 문 탈출

    # 현재까지 찾은 best와 그때의 비용을 반환
    return current, valueC

def randomInit(p): # o   
    # Return a random initial tour
    numCities = p[0]
    init = list(range(numCities))
    # for i in range(0,p[0]):##체크
    #     init.append(i)
    random.shuffle(init)
    return init


def evaluate(current, p): # o
    ## current : 도시 방문 인덱스 순서
    global NumEval
    NumEval += 1
    cost = 0
    table = p[2]
    for i in range(0,len(current)-1):
        cost += table[current[i]][current[i+1]]
    cost = round(cost,1)
    return cost


def mutants(current, p): # Apply inversion
    triedPairs = []
    neighbors = []
    numCities = p[0]
    while len(triedPairs)<numCities:
        i,j = random.randint(0,numCities-1),random.randint(0,numCities-1) # 숫자 1개
        if i>j:
            i,j = j,i
        if [i,j] not in triedPairs:
            triedPairs.append([i,j])
        else:
            continue
    for i in triedPairs:
        neighbors.append(inversion(current,i[0],i[1]))
    return neighbors

# 방법1
# def inversion(current, i, j):  ## Perform inversion
#     curCopy = current[:]
#     temp = curCopy[i]
#     Cth = abs(j-i)
#     for k in range(Cth):
#         change(curCopy,i+Cth,j-Cth)
#     return curCopy
# def change(current,i,j):
#     tpCur = current[:]
#     temp = tpCur[i]
#     tpCur[i] = tpCur[j]
#     tpCur[j] = temp
#     return tpCur

# 방법 2
# def inversion(current, i, j):
#     curCopy = current[:]
#     while i < j:
#         curCopy[i],curCopy[j] = curCopy[j],curCopy[i]
#         i+=1
#         j-=1


def inversion(current, i, j):
    curCopy = current[:]
    temp = curCopy[i:j+1]
    temp.reverse()
    curCopy[i:j+1] = temp
    return curCopy


def bestOf(neighbors, p):   # x
    # neighbots 중 가장 cost가 작은 neighbor 선정
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
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()
