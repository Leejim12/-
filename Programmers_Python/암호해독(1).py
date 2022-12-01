# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:00:07 2022

@author: user
"""

## 인덱스 번호는 +1
def solution(cipher, code):
    answer = ''
    for i in range(code-1,len(cipher),code):
        answer = answer + cipher[i]
    return answer
