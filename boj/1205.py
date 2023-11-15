import sys
import bisect
r = sys.stdin.readline
n,score,rank = map(int,r().strip().split())
if n:
    x = sorted(map(int,r().strip().split()))
    if n==rank and x[0]>=score:
        print(-1)
    else:
        ranking = (n+1)-bisect.bisect_right(x,score)
        print(ranking if ranking<= rank else -1)
else:
    print(1)