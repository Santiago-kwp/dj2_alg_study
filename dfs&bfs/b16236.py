# 아기상어
d = [0, 0, -1, 1]
def check_empty(size):
    for i in range(N):
        for j in range(N):
            if arr[i][j] and arr[i][j] <= size: return 0
    return 1
def bfs(Q, size, eat, dst):
    for i, j in Q:    
        if check_empty(size): return dst
        for k in range(4):
            ni, nj = i+d[k], j+d[k-2]
        if ni in range(N) and nj in range(N):
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                # 빈 칸인 경우 그냥 이동
                if not arr[ni][nj]:
                    bfs(ni, nj, size, eat, dst+1)
                # 빈칸은 아니고 먹을 수 있는 경우
                elif arr[ni][nj] <= size:
                    arr[ni][nj] = 0
                    if eat == size-1:
                        bfs(ni, nj, size+1, 0, dst+1)
                    else:
                        bfs(ni, nj, size, eat+1, dst+1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            visited[i][j] = 1
            bfs([(i, j)], 2, 0, 0)