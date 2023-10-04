import sys
row,col = map(int,sys.stdin.readline().split())
d = {'L' : (0,-1), 'R':(0,1),'D':(1,0),'U':(-1,0)}
m,M = [],[]
res = 0
route = 0
for i in range(row):
    m.append(sys.stdin.readline().strip())
    M.append([0]*col)
for Row in range(row):
    for Col in range(col):
        if not M[Row][Col]:
            route+=1
            r,c = Row,Col
            while not M[r][c]:
                M[r][c]=route
                direction = m[r][c]
                dr,dc=d[direction]
                r+=dr
                c+=dc
            res+=1 if M[r][c]==route else 0
print(res)