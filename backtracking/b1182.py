# 부분수열의 합, 가지치기 하려고 했으나 경우의 수가 2^20 이라 
# 그냥 완전탐색으로 부분집합의 수로 계산, 공집합을 제외하고 계산하는게 포인트 정도
def backtrack(i, s, n):
    global cnt
    if i == N:
        if s == S and n:
            cnt += 1
        return
    for c in [1, 0]:
        backtrack(i+1, s+arr[i]*c, n+c)
    
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
backtrack(0,0,0)
print(cnt)