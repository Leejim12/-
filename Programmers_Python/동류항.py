def solution(polynomial):
    k = polynomial.split(' + ')
    print(k)
    add = []
    num = []
    for i in k:
        if i[len(i)-1] == 'x':
            add.append(i)
        else:
            num.append(i)
    x = 0
    for i in add:
        if(i[0:(len(i)-1)]==''):
            x = x + 1
        else:
            x = x + int(i[0:(len(i)-1)])     
    n = 0
    for i in num:
        n = n + (int)(i)
    if(x==0):
        answer = str(n)
    elif(x==1):
        if(n==0):
            answer = 'x'
        else:
            answer = 'x + ' + str(n)
    elif(n==0):
        answer = str(x)+'x'
    else:
        answer = str(x)+'x + '+str(n)
    return answer


aaa = "x + 1"
print(solution(aaa))