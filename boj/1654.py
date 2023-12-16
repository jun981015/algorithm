#https://www.acmicpc.net/problem/1654
import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
lan = []
for n in range(n):
    lan.append(int(sys.stdin.readline().rstrip()))
lan.sort(reverse=True)
m = 1
M = lan[0]+1
answer = 0
while m<M:
    s= 0 
    mid = (M+m)//2
    for line in lan:
        s+= line//mid
    if s<k:
        M = mid
    else:
        answer = mid
        m = mid+1
print(answer)