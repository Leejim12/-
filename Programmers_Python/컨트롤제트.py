def solution(s):
    answer = 0
    temp = s.split()
    for i in range(0,len(temp)):
        if(temp[i]=='Z'):
            temp[i]=0
            if(i!=0):
                temp[i-1]=0
    for j in temp:
        answer = answer + (int)(j)
    return answer