# 20058 마법사 상어와 파이어스톰
d = [0, 0, -1, 1]
def bfs(Q):
    ice = 1
    for i, j in Q:
        for k in range(4):
            ni, nj = i+d[k], j+d[k-2]
            if ni in range(N) and nj in range(N):
                if arr[ni][nj]: 
                    arr[ni][nj] = 0
                    Q+=[(ni, nj)]
                    ice += 1
    return ice


# N : 2**N 격자, Q : 파이어스톰 시전 수
N, Q = map(int,input().split())
N = 2**N
arr = [list(map(int, input().split())) for _ in range(N)]

# 마법사 상어가 시전한 단계
step = list(map(int, input().split()))

# 해야 될 것
# 1. 먼저 격자를 2**L x 2**L 로 나누기
# 2. 시계방향으로 90도 회전

arr_new = [[0]*N for _ in range(N)]
for s in step:
    for i in range(0, N, 2**s):
        for j in range(0, N, 2**s):
            for k in range(i, i+2**s):
                for l in range(j, j+2**s):
                    arr_new[l+i-j][i+j+2**s-k-1] = arr[k][l]

    melt = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                ni, nj = i+d[k], j+d[k-2]
                if ni in range(N) and nj in range(N) and arr_new[ni][nj]:
                    cnt += 1
            if cnt < 3:
                melt[i][j] = 1
    
    for i in range(N):
        for j in range(N):
            arr[i][j] = max(arr_new[i][j] - melt[i][j], 0)

print(sum([sum(arr[i]) for i in range(N)]))
bigice = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            arr[i][j] = 0
            bigice = max(bigice, bfs([(i, j)]))

print(bigice)
