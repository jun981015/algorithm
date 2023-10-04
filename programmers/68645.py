#https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    num = int(n*(n+1)/2)
    index,stair,change,iter = 1,0,0,0
    answer = [0]+[0]*num
    state = [1,0,-1]
    for number in range(1,num+1):
        if iter==n:
            n-=1
            change+=1
            iter=0
        iter+=1
        s = state[change%3]
        index += s*stair if s else 1
        stair += s
        answer[index]=number
    answer.pop(0)
    return answer