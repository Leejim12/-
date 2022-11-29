# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:12:41 2022

@author: user
"""

###################### CSV 파일 읽기 ###############################
## 1. csv 파일 읽기
import csv,os
os.chdir(r'C:\Users\user\Python_data\ch04')
f=open('a.csv','r')
# 안열리면 f=open('a.csv','r',encoding="utf-8)

## 2. 파이썬에서 읽기 -> csv.reader
new = csv.reader(f)
new
for i in new:
    print("메소드",i)
    ## 객체가 2개임 : [1],[2]

## 3. csv형 List로 변경
a_list = []
f.seek(0) # 커서 처음으로 이동
for i in new:
    a_list.append(i)
    # 2의 반복문에서 커서가 마지막으로 이동했기 때문에, a_list가 텅 비어있음.
f.seek(0)
for i in a_list:
    print("a_list",i)

## 4. opencsv함수
def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    f.close()

k = opencsv('example2.csv')
for i in k:
    print("k",i)
    
###################### CSV 파일 쓰기 ###############################

# 1. CSV형 리스트로 만들어서 객체에 저장
a = [
     ['구','전체','내국인','외국인']
     ['관악구','519864','502089','17775']
     ['관악구','519864','502089','17775']
     ['관악구','519864','502089','17775']
     ]

# 2. 쓰기 모드
f = open('abc.csv','w',newline='') 
    # newline='' : 이거 안해주면 줄바꿈 한번 더 일어남(이유 -> 참고1)

# 3. cs.writer() : csv형 리스트를 파일에 쓸 수 있게 해줌.
csvobject = csv.writer(f,delimiter=',')
    # 구분자가 ;라면 delimiter=';'

# 4. csv파일 안에 csv형 리스트 저장
csvobject.writerows(a)
f.close()

# 5. writecsv 함수
def writecsv(filename,the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

