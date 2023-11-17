import sys
r = sys.stdin.readline
n = int(r())
switches =list(map(int,r().split()))
s =int(r())
for i in range(s):
    sex, num = map(int,r().split())
    if sex==1:
        for idx in range(num,n+1,num):
            switches[idx-1] = 0 if switches[idx-1] else 1
    else:
        for idx in range(min(num,n+1-num)):
            if switches[num-1-idx]==switches[num-1+idx]:
                x = 0 if switches[num-1-idx] else 1
                switches[num-1-idx],switches[num-1+idx] = x,x
            else:
                break
for i in range(n//20+1):
    print(' '.join([str(_) for _ in switches[20*i:20*(i+1)]]))