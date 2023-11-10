import sys
import itertools
from math import inf
n = int(sys.stdin.readline())-1 
num_array = list(map(int,sys.stdin.readline().split()))
oper = list(map(int,sys.stdin.readline().split()))
m,M = inf,-inf
o = ''
for i,j in zip(oper,['+','-','*','/']):
    o+=j*i
operators = set(itertools.permutations(o,n))
for operator in operators:
    s = num_array[0]
    for n,o in zip(num_array[1:],operator):
        if o=='+':
            s+=n
        elif o =='-':
            s-=n
        elif o =='*':
            s*=n
        else:
            s = -(-s//n) if s<0 else s//n
    m=min(m,s)
    M=max(M,s)
print(M)
print(m)