# 선형 큐 활용
di = [-1, 1, 0, 0, -1, 1, -1, 1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i, j):
    front, rear = -1, 0
    Q[rear] = (i, j)
    maps[i][j] = 0
    while front != rear:
        front += 1
        i, j = Q[front]
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
            if maps[ni][nj]:
                maps[ni][nj] = 0
                rear += 1
                Q[rear] = (ni, nj)
    
while 1:
    w, h = map(int, input().split())
    if not h: break
    maps = [list(map(int, input().split())) for _ in range(h)]
    Q = [0]*(w*h)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)

# DFS 재귀 한도 초과시키고 통과하기 8방향 탐색?! 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
# import sys
# sys.setrecursionlimit(10**9)
di = [-1, 1, 0, 0, -1, 1, -1, 1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]
def dfs(i, j):
    visited[i][j] = 1
    for k in range(8):
        ni, nj = i+di[k], j+dj[k]
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if not visited[ni][nj] and maps[ni][nj]:
            dfs(ni, nj)

while 1:
    w, h = map(int, input().split())
    if not h: break
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)