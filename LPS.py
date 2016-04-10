"""
Created on Fri Apr 08 17:53:15 2016

@author: ASU_CUDA_LAPTOP
"""

#Longest palindrome subsequence
string = "BABCBAB"
n = len(string)
p = [[0 for _ in range(len(string))]for _ in range(len(string))]
for i in range(n):
    p[i][i] = 1;
for var in range(2, len(string) + 1):
    for i in range(0, n-var+1):
        j =  i+var-1      
        if((string[i] != string[j])):            
                p[i][j] = max(p[i+1][j], p[i][j-1]);            
        elif((string[i] == string[j]) and (j-i) == 1):  #2 elements
                p[i][j] = 2
        elif(string[i] == string[j]): #Miscellenous length
            p[i][j] = 2+p[i+1][j-1]
