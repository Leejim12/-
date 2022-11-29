# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:05:03 2022

@author: user
"""
import os
import usecsv
os.chdir(r'C:\공부\11가지 프로젝트로 시작하는 파이썬 생활 프로그래밍')
a=[['국','영','수'],[99,88,77]]
usecsv.writecsv('test.csv', a)
