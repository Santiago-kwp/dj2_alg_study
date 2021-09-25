# 익은 토마토를 첫 큐에 다 넣고, BFS를 돌면서 거리를 계산하며 최대 거리를 반환

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
Q = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q += [(i,j)]

# BFS using linear Q
for i, j in Q:
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < M and not tomato[ni][nj]:
            if tomato[ni][nj] != -1:
                tomato[ni][nj] = tomato[i][j] + 1
                Q += [(ni, nj)]

max_d = 0
for i in range(N):
    if max_d < max(tomato[i]):
        max_d = max(tomato[i])
    if 0 in tomato[i]:
        max_d = 0
        break
print(max_d-1)
        
