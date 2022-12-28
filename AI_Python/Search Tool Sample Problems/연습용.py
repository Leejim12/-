# -*- coding: utf-8 -*-

def createProblem():
    proName = input("What kinda problem do you want to solve?()")
    file = open(proName + ".txt",'r')
    content = file.read()
    tp = content.split('\n') ## ?
    print('tp[0]',tp[0])
    expression = tp[0]
    varName = []
    low = []
    up = []
    domain = []
    for i in range(1,len(tp)-1):             ### 1~끝 : 
        ## [varName, low, up]
        # 1. content[i] ','단위로 찢기
        temp = tp[i].split(',')    ## [0] : varName, [1] : low, [2]: up
        print("temp",temp)
        varName.append(temp[0])
        low.append(eval(temp[1]))
        up.append(eval(temp[2]))
        ## templist = [varName, low, up] 일케 구성됨.
    domain.append(varName)
    domain.append(low)
    domain.append(up)
    print("expression",expression)
    print("domain",domain)
    file.close()
    return expression, domain

createProblem()
##################################