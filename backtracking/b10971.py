'''
재귀호출로 출발 정점부터 모든 정점을 다 돌았을 때
마지막 정점과 출발 정점이 연결되어 있으면 더한 값의 최소 값을 갱신
minw 변수를 통해 중간 가지치기
'''
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

minw = 1E10
def dfs(i, s, st):
    global minw
    if minw < s+W[i][st]:
        return
    if sum(v) == N and W[i][st]:
        minw = min(minw, s+W[i][st])
    for j in range(N):
        if W[i][j] and not v[j]:
            v[j] = 1
            dfs(j,s+W[i][j], st)
            v[j] = 0
            
for i in range(N):
    v = [0]*N
    v[i] = 1
    dfs(i,0,i)
print(minw)
