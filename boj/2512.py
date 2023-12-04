n = int(input())
cities =sorted(map(int,input().split()))
budget = int(input())
for i in cities:
    if i*n<=budget:
        answer=i
        budget-=i
        n-=1
    else:
        answer = budget//n
        break
print(answer)