#greedy, heapq
import sys
import heapq
import random
random.seed(1)
def random_example(n,m):
    l = []
    for i in range(n):
        s = random.randint(0,int(1e2))
        t = random.randint(s+1,int(1e2)+1)
        l.append((s,t))
    return l

def main():
    input = sys.stdin.readline
    n = int(input())
    lectures = [tuple(map(int, input().split())) for _ in range(n)]
    # lectures = random_example(10,2)
    lectures.sort(key=lambda x: x[0])
    
    heap = []
    for s, e in lectures:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    print(len(heap))

if __name__ == '__main__':
    main()
