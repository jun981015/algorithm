import sys
from collections import defaultdict,Counter
r = sys.stdin.readline
t = int(r())
ans=[]
for i in range(t):
    d=defaultdict(list)
    winner,score,fifth = None,1e6,1e6
    _,c=r(),r().split()
    count = Counter(c)
    s=1
    for team in c:
        if count[team]>=6:
            d[team].append(s)
            s+=1
    del count,c
    for key in d.keys():
        s=sum(d[key][:4])
        if s<score:
            score=s
            fifth=d[key][4]
            winner=key
        elif s==score and d[key][4]<fifth:
            winner=key
            fifth=d[key][4]
    ans.append(winner)
for i in ans:
    print(i)