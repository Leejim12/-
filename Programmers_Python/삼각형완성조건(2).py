# 삼각형의 완성 조건
def chk(TB,i):
    PR=[]
    PR.append(TB[0])
    PR.append(TB[1])
    PR.append(i)
    PR.sort()
    #print("PR",i,PR)
    if(PR[0]+PR[1]>PR[2]):
        return True
    else:
        return False
    #PR = []
def solution(sides):
    answer = 0
    sides.sort()
    print(sides)
    for i in range(1,sides[0]+sides[1]):
        print(i,chk(sides,i))
        if(chk(sides, i))==True:
            answer = answer + 1
        else:
            pass
    return answer

    
    
ex = [11, 7]
print(solution(ex))
#### PR = TB로 하고 PR을 처리해도, TB가 같이 바뀐다.
#### 포인터 관련 개념인듯.