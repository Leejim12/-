# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:57:45 2022

@author: user
"""

def solution(numbers, k):
    t = -1
    t = t+2*k
    answer = t%len(numbers)
    return answer

n = [1, 2, 3, 4, 5, 6]
tk = 5
solution(n,tk)


