# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:17:56 2022

@author: user
"""
def solution(dot):
    answer = 0
    if dot[0]>0:
        if dot[1]>0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1]>0:
            answer = 2
        else:
            answer = 3
    return answer

tpdot = [1,2]
solution(tpdot)

## dot : location for the dot



