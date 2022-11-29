# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:10:54 2022

@author: user
"""
##### AlterDataType
import os,re
import usecsv

os.chdir(r'C:\공부\11가지 프로젝트로 시작하는 파이썬 생활 프로그래밍\Ch04')
total = usecsv.opencsv('popSeoul.csv')    
############# (Pra) Type Casting and deleteing ',' #############
## Example of useing 'float()'
'''
i = '123'
float(i)
int(i)

## re.sub(',',,j)
j = '1,468,146'
k = float(re.sub(',', '', j))
type(k)'''
###########################################################

## Changing just one row in total
i = total[2]
i
k = []
for j in i:
    if re.search('[a-z가-힣!]',j): #if there r alphbet of korean literature
        # ! : Special words
        k.append(j)
    else:
        k.append(float(re.sub(',','',j)))
k
#### Not making k
i = ['123!!','151,767','11,093','27,394','']
for j in i:
    if re.search('[a-z가-힣!]', j):
        i[i.index(j)]=j
    else:
        try: #### Treating Exception
            i[i.index(j)]=(float(re.sub(',', '', j)))
        except:
            pass
## main
total
#### Pra
i = total[1]
for j in i:
    try:
        i[i.index(j)] = float(re.sub(',', '', j))
    except:
        pass

#### Real main
for i in total:
    for j in i:
        try:
            i[i.index(j)]=float(re.sub(',','',j))
        except:
            pass



