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


####################################### 참고할 만한 숏코딩
i, r = input, range
n = int(i())
m, s = [[*i()] for _ in r(n)], 'RG'

c, v = 0, [[0] * n for _ in r(n)]
d, w = 0, [[0] * n for _ in r(n)]


def p(a, b, c, d):
    q, v[a][b] = [(a, b)], 1
    for i, j in q:      # 선형 큐를 정의하는 대신 for문을 이용해서 q가 계속 append 되는것을 활용한 코드
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < n and 0 <= y < n and not d[x][y] and m[x][y] in c:
                d[x][y] = 1
                q += [(x, y)]


for i in r(n):
    for j in r(n):
        if not v[i][j]:
            c += 1
            p(i, j, m[i][j], v)
        if not w[i][j]:
            t = m[i][j]
            d += 1
            p(i, j, s if t in s else t, w) #R 이나 G 인 경우에는 RG를 보내서 `in` 으로 같은지 여부를 확인

print(c, d)