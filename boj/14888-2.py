import sys
r = sys.stdin.readline
n = int(r().strip())
num_array = list(map(int,r().split()))
oper = list(map(int,r().split()))
m,M = 1e9,-1e9
def f(num, index, add, sub, mul, div):
    global m,M
    if index==n-1:
        m ,M= min(num,m),max(num,M)
        return None
    index+=1
    if add>0:
        f(num+num_array[index], index, add-1, sub, mul, div)
    if sub>0:
        f(num-num_array[index], index, add, sub-1, mul, div)
    if mul>0:
        f(num*num_array[index],index, add, sub, mul-1, div)
    if div>0:
        f(num//num_array[index] if num>0 else -(-num//num_array[index])\
            , index, add, sub, mul, div-1)
f(num_array[0],0,*oper)
print(M)
print(m)