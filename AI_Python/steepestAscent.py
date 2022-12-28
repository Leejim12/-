from problem_skeleton import Numeric as k

def main():
# Numeric class instance 생성
  NC = k()
  
# setVariable 이용해 문제 읽어옴
  NC.setVariables
# steepestAscent 실행
  steepestAscent(NC)
# describe, report 이용 결과 출력
  NC.describe()
  NC.report()
  NC.coordinate()


def steepestAscent(NC):
    current = NC.randomInit()
    valueC = NC.evaluate(current)
    while True:
        neighbors = NC.mutants(current)
        # 각각의 neighbor에 대해 함수 값 계산 => 더 좋은거 있으면 이동
        best, bestValue = bestOf(neighbors)
        if bestValue < valueC:
          current = best
          valueC = bestValue
        else:
          break
    NC.storeResult()

def bestOf(neighbors, p):
    # 1. 가장 처음 sample을 best라 가정.
    # 2. 두 번째 부터 계속 비교하면서 더 좋은게 찾아지면 best로 저장해 둔다.
    # 3. 모두 다 비교 끝나면 best 반환
    best = neighbors[0]
    bestValue = k.evaluate(best,p)
    
    for i in range(1,len(neighbors)):
        newValue = k.evaluate(neighbors[i],p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def displaySetting(NC):
    NC = k()
    print()
    print("Search algorithm: Graduent Descent")
    print()
    print("Mutation step size:", NC.getDelta())


main()