#https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    for i in range(len(triangle)-1,0,-1):
        for j in range(0,i): triangle[i-1][j]+=max(triangle[i][j:j+2])
    return triangle[0][0]