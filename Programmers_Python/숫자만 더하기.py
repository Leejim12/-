# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:50:40 2022

@author: user
"""
import re

def solution(my_string):
    answer = 0
    temp = re.split('[A-Z,a-z]', my_string)
    print(temp)
    for i in temp:
        try:
            answer = answer + (int)(i)
        except:
            pass
    return answer


s = "aAb1B2cC34oOp"
print(solution(s))