#https://school.programmers.co.kr/learn/courses/30/lessons/12902#
def solution(n):
    if n%2 : return 0
    else:
        dp = [2]*(n//2)
        dp[0]=3
        s = 0 
        for i in range(n//2-1):
            dp[i+1] += (dp[i]*3 +s)%1000000007
            s+=dp[i]*2%1000000007
    return dp[-1]
