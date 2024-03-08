s1 = input()
s2 = input()
d = [[0]*(len(s1)+1) for i in range(len(s2)+1)]
for i in range(0,len(s2)+1):
    for j in range(0,len(s1)+1):
        if i==0 or j==0:
            d[i][j]=0
        elif s1[j-1]==s2[i-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])
print(d[-1][-1])