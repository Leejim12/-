# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:24:55 2022

@author: user
"""
## MakingToTwoDimension
## My Solution
'''
def solution(num_list, n):
    answer = [[]]
    temp = []
    for i in range(len(num_list)):        
        if (i+1)%n==0:
            temp.append(num_list[i])
            answer.append(temp)
            temp = []
        else:
            temp.append(num_list[i])
    ## in the first index, there remain [] so use it.
    answer.remove([])
    return answer
'''

## High Level 
def solution(num_list,n):
    return [num_list[ix-n:ix] for ix in range(n,len(num_list)+1,n)]

ttt = [100, 95, 2, 4, 5, 6, 18, 33, 948]
tn = 3

solution(ttt,tn)
