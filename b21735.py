# 1초 동안 할 수 있는 플레이 
# 1. +1 칸 가서 +1 칸의 눈덩이 추가 하기
# 2. +2 칸 가서 반으로 줄이고 +2 칸의 눈덩이 추가하기
# 접근 => 깊이 우선 탐색하여 완전 탐색 후 최대값 비교
N, M = map(int, input().split())
a = [0]+list(map(int, input().split()))
total = []
def dfs(idx, snow, M):
    if not M or idx==N:
        total.append(snow)
        return
    else:
        if idx <= N-1:
            dfs(idx+1,snow+a[idx+1], M-1)
        if idx <= N-2:
            dfs(idx+2,snow//2 + a[idx+2], M-1)
dfs(0, 1, M)
print(max(total))
