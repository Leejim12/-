# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:52:40 2022

@author: user
"""

def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(2,n-1):
            if(i%j==0 and i!=j):
                print(i,j)
                answer = answer + 1
                break
    return answer


solution(10)