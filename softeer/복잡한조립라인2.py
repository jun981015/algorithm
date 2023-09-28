#https://softeer.ai/practice/info.do?idx=1&eid=405
import sys
K,N =map(int,sys.stdin.readline().strip().split())
time = [0]*K
move = 0
for col in range(N-1):
    n = list(map(int,sys.stdin.readline().strip().split()))
    if K!=1: move = n.pop()
    for row in range(K): time[row]+=n[row]
    min_time = min(time)
    for row in range(K): time[row] = min(time[row],min_time+move)
n = list(map(int,sys.stdin.readline().strip().split()))
for row in range(K):
    time[row]+=n[row]
print(min(time))
