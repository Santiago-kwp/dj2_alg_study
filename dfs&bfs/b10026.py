# 선형 큐 활용
# BFS -> 같은 색의 구간을 찾고 방문 체크
# BFS 한번 들어갔다 나올 때마다 구간 + 1
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(i, j, arr):
    Q = [0]*(N**2)
    front, rear = -1, 0
    Q[rear] = (i, j)
    visited[i][j] = 1
    while front!=rear:
        front += 1
        i, j = Q[front]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0<= nj < N:
                if not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                    visited[ni][nj] = 1
                    rear += 1
                    Q[rear] = (ni, nj)

N = int(input())
arr = [input() for _ in range(N)]
arr2 = [x.replace('R','G') for x in arr]

cnt = cnt2 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j, arr)
            cnt += 1

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j, arr2)
            cnt2 += 1

print(cnt, cnt2)