# 사업성 분석
import numpy_financial as np
import usecsv

def presentvalue(n):
    dicount = .05
    cashflow = 100
    return (cashflow/(1+dicount)**n)


print(presentvalue(1))
print(presentvalue(2))

for i in range(20):
    print(presentvalue(i))

## 놀이공원
loss = [-750,-250]
profit = [100]*18
profit

cf = loss + profit
cf
len(cf)
    ## 일반 리스트끼리 덧셈은 이렇게 된다.
    
cashflow = np.array(cf)

## np.npv(할인율,현금흐름) : 순현재가치
## np.irr(현금흐름) : 내부수익률

npv = np.npv(0.045,cashflow)

