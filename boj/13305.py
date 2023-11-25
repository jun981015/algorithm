#https://www.acmicpc.net/problem/13305
n,dist = input(),list(map(int,input().split()))
_ = list(map(int,input().split()))[:-1]
gas = [i for i in enumerate(_)]
gas.sort(key = lambda x:x[1])
budget = 0
visit = len(dist)+1
for city,cost in gas:
    if city<visit:
        budget+=sum(dist[city:visit])*cost
        visit=city
print(budget)