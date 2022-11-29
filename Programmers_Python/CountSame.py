# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:40:09 2022

@author: user
"""
def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if(i == j):
                answer=answer+1
    return answer
