def solution(n):
    k = list(range(1,300))
    for i in k:
        if(i%3==0):
            k.remove(i)
    answer = k[n+1]
    return answer