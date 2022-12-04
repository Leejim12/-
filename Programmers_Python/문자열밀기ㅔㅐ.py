## 문자열 밀기
def push(A):
    rt = ""
    tp1 = list(A)
    tp2 = []
    tp2.append(tp1[len(tp1)-1])
    for i in range(0,len(tp1)-1):
        tp2.append(tp1[i])
    for i in tp2:
        rt = rt + i
    return rt

def solution(A, B):
    answer = 0
    if(A==B):
        return 0
    for i in range(0,len(A)):
        A = push(A)
        answer = answer + 1
        if(A==B):
            return answer
    return -1


A = "hello"
B = "ohell"
print(solution(A,B))