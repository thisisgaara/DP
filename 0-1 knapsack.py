# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 17:40:52 2016

@author: ASU_CUDA_LAPTOP
"""

# 0-1 knapsack
wt = [1, 3, 4, 5]
val = [1,4,5,7]
target = 7
dp= [[0 for _ in range(0, target+1)]for _ in range(0, len(wt)+1)]
for i in range (0, len(wt)):
    for j in range(0, target + 1):
        if((j == 0)):
            dp[i][j] = 0
        elif(i ==0):
            dp[i][j] = wt[i]
        elif wt[i] <= j:
            dp[i][j]= max(val[i] + dp[i-1][j - wt[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
"""

"""
