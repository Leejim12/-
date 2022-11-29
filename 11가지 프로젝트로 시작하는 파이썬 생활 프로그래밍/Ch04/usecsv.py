# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:02:43 2022

@author: user
"""
import csv,os,re

def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    f.close()
    return output

def writecsv(filename,the_list):
    with open(filename,'w',newline='') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
## Abaconda3>Lib에 usscsv.py를 넣으면, os 나 re 모듈처럼 사용할 수 있음.

def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return listname
                                      
