# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = [10,22,9,33,21,50,41,60,80]
t = [1 for _ in range(len(a))]
for i in range (1, len(a)):
    max_val = -32767
    for j in range(0, i):
        if(a[j] < a[i]):
            max_val = max(max_val, 1+t[j])
    if(max_val > 0):
        t[i] = max_val
    pass    

output = [0 for _ in range(t[len(t)-1]+1)]
#Below code is to print the subsequence
for j in range(len(t)-1, -1, -1):
    output[t[j]] = a[j]
    
