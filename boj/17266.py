length,n = int(input()),int(input())
lights = list(map(int,input().split()))
light ,height = 0,0
between = []
if n>1:
    for i in range(n-1):
        height = max(sum(divmod(lights[i+1]-lights[i],2)),height)
s,e = lights[0],length-lights[-1]
height = max(height,s,e)
print(height)