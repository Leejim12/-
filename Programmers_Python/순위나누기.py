
def solution(score):
    ## answer : 0 배열
    tp = []
    pra = []
    ## tp : 총점 배열
    for i in score:
        tp.append(sum(i[0],i[1])

    for i in tp:
        pra.append(i)
    ## table : 점수에 따른 순위
    table = []
    for i in range(0,len(tp)):
        table.append([i+1,max(pra)]) ##[1등,190점]
        pra[pra.index(max(pra))]=0
    return answer