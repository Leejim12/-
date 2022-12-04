
def solution(score):
    ## answer : 0 배열
    answer = []
    tp = []
    pra = []
    ## tp : 총점 배열
    for i in score:
        tp.append(i[0]+i[1])
    for i in tp:
        pra.append(i)
    ## table : 점수에 따른 순위
    table = []
    for i in range(0,len(tp)):
        table.append([i+1,max(pra)]) ##[1등,190점]
        pra[pra.index(max(pra))]=0
    print(table)
    for i in range(0,len(table)-1):
        if(table[i][1]==table[i+1][1]):
            table[i+1][0] = table[i][0]
    for i in tp:
        for j in table:
            if(i==j[1]):
                answer.append(j[0])
                break
    return answer

ex1 = [[80, 70], [90, 50], [40, 70], [50, 80]]
print(solution(ex1))