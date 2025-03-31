import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split()) # n = row, m = col
MAP = []
for _ in range(n):
    row = list(str(input().rstrip()))
    MAP.append(list(map(int, row)))
moves = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]]
visited = [[[0]*m for i in range(n)] for j in range(2)]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        Break, row, col = q.popleft()
        if row == n - 1 and col == m - 1:
            return visited[Break][row][col]
        dist = visited[Break][row][col]
        for _ in moves:
            dr, dc = _
            nrow, ncol = row+dr,col+dc
            if 0 <= nrow < n and 0 <= ncol < m:
                if MAP[nrow][ncol] == 0 and visited[Break][nrow][ncol] == 0:
                    visited[Break][nrow][ncol] = dist + 1
                    q.append([Break, nrow, ncol])
                elif MAP[nrow][ncol] == 1 and Break == 0:
                    visited[not Break][nrow][ncol] = dist + 1
                    q.append([not Break, nrow, ncol])
    return -1

print(bfs())