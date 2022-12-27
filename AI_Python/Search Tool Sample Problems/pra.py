def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'expression'은 txt 파일의 첫 줄에 있는 수식 string
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## txt 파일의 두 번째 줄 부터는 변수명,최소값,최대값
    ## 'varNames' is a list of variable names.
    ## 'varNames'는 각 변수의 이름이 저장 됨
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'low'에는 각 변수의 최소값이 저장됨
    ## 'up' is a list of upper bounds of the varaibles.
    ## 'up'에는 각 변수의 최대값이 저장됨
    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    # readline()을 이용해 각 줄의 정보를 읽어옴
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
    ## 수식(String),
    
    a = createProblem()
    
    print(a)