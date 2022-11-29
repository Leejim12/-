# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:42:35 2022

@author: user
"""
## Analyze datas in CSV file
#### Main : Saving Impormations which is over 3% about the rate of forigen(Gu)
import os,re,usecsv

os.chdir(r'C:\공부\11가지 프로젝트로 시작하는 파이썬 생활 프로그래밍\Ch04')
'''
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)
print(newPop[:4])

#### Pra
ii = newPop[0]
ii
i = newPop[1]
i
i[2]
i[2]*100/(i[1]+i[2]) ## calculate rate of forigen who is living in specific Gu
foreign = round(i[2]*100/(i[1]+i[2]),1)
foreign

## For each gu, Calculate all of the foreign
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]*100/(i[1]+i[2]),1)
        print(i[0],foreign)
    except:
        pass
    
## new 
new =[['Gu','Korean','Foreign','Rate Of Foreign(%)']]

i
new.append([i[0],i[1],i[2],foreign])
new
'''
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)
for i in newPop:
    forigen = 0
    try:
        foreign = round(i[2]*100/(i[1]+i[2]),1)
        if foreign > 3:
            print(i[0],i[1],i[2],foreign)
    except:
        pass

new = [['Gu','Korean','Foreign','Rate Of Foreign(%)']]
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]*100/(i[1]+i[2]),1)
        if foreign > 3:
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass
    
usecsv.writecsv('newPop.csv', new)




