import sys
game = {"Y" : 2, "F" : 3, "O" : 4}
users = set()
r = sys.stdin.readline
n,g = r().split()
count,ans=1,0
for i in range(int(n)):
    user = r()
    if user not in users:
        users.add(user)
        count+=1
        if count==game[g]:
            ans+=1
            count=1
print(ans)