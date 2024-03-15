import bisect
N = int(input())
crane = sorted(list(map(int,input().split())), reverse=True)
box = int(input())
boxex = sorted(list(map(int,input().split())))
answer = 0
if crane[0]<boxex[-1]:
    print(-1)
    exit()
while boxex:
    for c in crane:
        if boxex and boxex[0] >c:
            pass
        elif boxex:
            idx = bisect.bisect_right(boxex,c)
            del boxex[idx-1]
    answer+=1
print(answer)