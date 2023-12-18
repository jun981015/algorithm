def prime_numbers(n):
    arr = [i for i in range(n+1)] 
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i): 
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]
n = int(input())
prime = prime_numbers(n)
start = 0
s = 0
idx = 0
answer=0
while start<len(prime) :
    s+=prime[idx]
    if s == n:
        answer+=1
    if s>n:
        s-=prime[idx]
        s-=prime[start]
        start+=1
    else:
        idx+=1
        idx = min(len(prime)-1,idx)
print(answer)