import sys
from collections import defaultdict
r = sys.stdin.readline
num,n =map(int,r().split())
ans = set()
d = defaultdict(set)
for i in range(num):
    _= r().strip()
    info = _.split()
    team,medals =int(info.pop(0)), ' '.join(info)
    d[medals].add(team)
    ans.add(medals)
ans = sorted(ans,reverse=1,key = lambda x : list(map(int,x.split())))
r = 1
for i in ans:
    if n in d[i]:
        print(r)
        break
    r+=len(d[i])