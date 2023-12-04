import sys
from collections import defaultdict
words = defaultdict(int)
input = sys.stdin.readline
n, length = map(int,input().strip().split())
M = -1
for i in range(n):
    word = input().strip()
    if len(word)>=length:
        words[word]+=1
        M = max(M,len(word))
ans = sorted(words.items(),key = lambda x:x[1],reverse=True) 
words = defaultdict(list)
for word,num in ans: words[num].append(word)
answer = []
for i in words:
    temp = sorted(words[i])
    temp2 = {i : [] for i in range(M,length-1,-1)}
    for i in temp: temp2[len(i)].append(i)
    for i in temp2.values(): answer+=sorted(i)
for i in answer:
    print(i)