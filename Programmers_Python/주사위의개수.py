# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:42:40 2022

@author: user
"""

def solution(box, n):
    answer = (box[0]//n)*(box[1]//n)*(box[2]//n)
    return answer