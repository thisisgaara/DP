# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
"""
print Fibonacci sequence
0 1 1 2 3 5 8 13 21 34 55.. .
"""

"""
#Normal iterative for loop

def fib(i):
    if(i == 0):
        return 0;
    x1 = 0
    x2 = 1
    for j in range(2, i+1):
        x3 = x1+x2
        x1 = x2;
        x2 = x3;
    return x2;     
   
"""
"""
#Recursion

print 0
print 1
def fib(i):
    if(i == 1):
       return 1;
    elif (i == 0):
        return 0;
    return (fib(i-1) + fib(i-2))

        
""" 
"""

f = [0,1];   
def stub():        
    i = 10    
    for j in range(2, i+1):
        f.append(f[j-1] + f[j-2]);   
stub();

#Memoization - 1
def fib(i):
      return f[i]  
"""
"""
#Memoization 2
f = [0 for i in range(0, 10)]
f[1] = 1;
def stub(j):
    global f
    if(j == 0):
        return 0;
    if (f[j]):
        return f[j]    
    f[j] = stub(j-1) + stub(j-2)
        
def fib(j):
    stub(j)
    return f[j]
"""
def fibonacci(i):
    for j in range(2, i):
        print fib(j);

fibonacci(10);


