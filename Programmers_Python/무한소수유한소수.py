def solution(a, b):
    if(a>b):
        tpn = b
    elif(a<b):
        tpn = a
    for i in range(2,tpn):
        if(a%i == 0 and b%i == 0):
            a = a//i
            b = b//i
        if(a%i == 0 and b%i == 0):
            a = a//i
            b = b//i
    print("a",a)
    print("b",b)
    for i in range(2,(int)(b+1)):
        if((int)(b)%i == 0 and (i%2!=0 and i%5!=0)):
            print("안되는 경우")
            print("b : ",b)
            print("i : ",i)
            print("i%2 : ",i%2)
            print("i%5 : ",i%5)
            return 2
    return 1

print(solution(12,36))