# 나이트의 이동 
di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]
def bfs(Q):
    for i, j in Q:
        if (i, j) == (oi, oj): return visited[i][j]-1
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(I) and nj in range(I) and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j]+1
                Q += [(ni, nj)]


for _ in range(int(input())):
    I = int(input())
    visited = [[0]*I for _ in range(I)]
    ci, cj = map(int, input().split())
    oi, oj = map(int, input().split())

    visited[ci][cj] = 1
    print(bfs([(ci, cj)]))

