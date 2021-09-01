'''
BFS로 접근하여 직사각형 전체를 1로 초기화 후 개별 직사각형을 0으로 설정
이중 for 문을 돌면서 1을 찾은 경우 bfs로 돌입=> 해당 좌표를 0으로 갱신 후 
4방향을 확인하면서 1의 개수를 세어 cnt에 누적
'''
N, M, K = map(int, input().split())
arr = [[1]*M for _ in range(N)]

for _ in range(K):
    xl, yl, xr, yr = map(int, input().split())
    for i in range(yl, yr):
        for j in range(xl, xr):
            arr[i][j] = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]       
ans = []
num = 0                             # 구획 수
for i in range(N):
    for j in range(M):
        if arr[i][j]:               # 나눠지는 구획의 시작
            arr[i][j] = 0
            num += 1
            q = [[i,j]]
            cnt = 0                 # 구획 내부 사각형 개수
            while q:
                i, j = q.pop(0)
                cnt += 1 
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if ni in range(N) and nj in range(M):
                        if arr[ni][nj]:
                            arr[ni][nj] = 0
                            q.append([ni,nj])
            if cnt:
                ans.append(cnt)
print(num)
print(*sorted(ans))