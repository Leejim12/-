## 옹알이
def solution(babbling):
    tp=[]
    All = ["aya", "ye", "woo", "ma",""]
    for i in All:
        for j in All:
            for k in All:
                for l in All:
                    for m in All:
                        tem = i+j+k+l+m
                        tp.append(tem)
    answer = 0
    for i in babbling:
        if i in tp:
            answer = answer + 1
    return answer

b = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(b))