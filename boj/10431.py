import sys
from bisect import bisect_left
r = sys.stdin.readline
n = int(r())
ans = dict()
for _ in range(n):
    students = list(map(int,r().split()))
    tc = students.pop(0)
    ans[tc]=0
    ordered = sorted(students)
    steps=0
    for i in range(19):
        m = ordered[i]
        idx = students.index(m)
        if i!=idx:
            temp = students[i]
            students.pop(idx)
            step = idx-i
            steps+=step
            students.insert(i,m)
    ans[tc]=steps
for i in ans:
    print(i,ans[i])
