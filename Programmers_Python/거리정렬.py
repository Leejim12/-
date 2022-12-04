def solution(numlist, n):
    answer = []
    disList = [] ## 거리,원숫자
    for i in numlist:
        disList.append([abs(i-n),i])
    disList.sort(key=lambda x:(x[0],-x[1]))
    for i in disList:
        answer.append(i[1])
    return answer

ex = [10000,20,36,47,40,6,10,7000]	
n = 30
print(solution(ex,n))