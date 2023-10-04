import bisect
import sys
n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for i in range(n)]
x.sort()
if n==1:
    print(0)
else:
    answer = 0
    while len(x)>2:
        k=x.pop(0)+x.pop(0)
        answer+=k
        idx = bisect.bisect_left(x,k)
        x.insert(idx,k)
    print(answer+sum(x))