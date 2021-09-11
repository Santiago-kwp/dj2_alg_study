'''
bfs로 접근해서 지나갈 길을 찾고, 지나온 길은 0으로 하고 큐에 대기열 걸어서 이후 길 찾기
'''
N = int(input())
zido = [[int(x) for x in input()] for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = []
num = 0
for i in range(N):
    for j in range(N):
        if zido[i][j]:
            zido[i][j] = 0
            num += 1
            q= [[i, j]]
            cnt = 0
            while q:
                r, c = q.pop(0)
                cnt += 1
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]
                    if nr in range(N) and nc in range(N):
                        if zido[nr][nc]:
                            zido[nr][nc] = 0
                            q.append([nr, nc])
            if cnt:
                ans.append(cnt)
print(num)
for t in sorted(ans):
    print(t)