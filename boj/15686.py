from itertools import combinations
from math import inf
import sys
size, store = map(int,sys.stdin.readline().strip().split())
house = dict()
chicken = dict()
h,c = 0,0
for i in range(size):
    row = list(map(int,sys.stdin.readline().strip().split()))
    for j in range(size):
        if row[j]==1:
            house[h] = (i,j)
            h+=1
        elif row[j]==2:
            chicken[c] =(i,j)
            c+=1
distance = {i : [] for i in chicken}
for i in distance:
    for j in house:
        y = abs(house[j][0]-chicken[i][0])
        x = abs(house[j][1]-chicken[i][1])
        distance[i].append(x+y)
minimun = inf
for comb in combinations(chicken,store):
    temp = []
    m = 0
    for i in comb: temp.append(distance[i])
    for dist in zip(*temp):
        m+=min(dist)
    if m<minimun:
        minimun=m
print(minimun)
