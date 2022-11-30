# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:54:52 2022

@author: user
"""
def fac(k):
    t = 1
    for i in range(1,k):
        t = t*i
    return t

def solution(n):
    answer = 0
    for i in range(13628800):
        if fac(i) > n:
            answer = i-2
            break
    return answer

solution(3628800)
