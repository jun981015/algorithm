#https://school.programmers.co.kr/learn/courses/30/lessons/68936
def f(arr):
    n = len(arr)
    s = sum([sum(i)for i in arr])
    if s==n*n: return [0,1]
    elif s==0: return [1,0]
    n=n//2
    return [sum(i) for i in zip(f([i[:n] for i in arr[:n]]),f([i[:n] for i in arr[n:]]),f([i[n:] for i in arr[:n]]),f([i[n:] for i in arr[n:]]))]
def solution(array):
    answer = f(array)
    return answer