'''
배추 심은 곳 1을 0으로 만들면서 bfs 탐색하며 cnt += 1
'''
d = [0,0,-1,1]
def bfs(Q):
    for i, j in Q:
        for k in range(4):
            ni, nj = i+d[k], j+d[k-2]
            if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
            if arr[ni][nj]:
                arr[ni][nj] = 0
                Q += [(ni, nj)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                arr[i][j] = 0
                bfs([(i, j)])
                cnt += 1
    print(cnt)

