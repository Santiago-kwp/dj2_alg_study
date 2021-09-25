'''
값이 1인 지역만 갈 수 있도록 하고 그 이전 칸에서 +1을 하여 거리를 갱신하는 BFS
'''
N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]

Q = [(0,0)]
for i, j in Q:
    for ni, nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if 0 <= ni < N and 0<= nj < M and arr[ni][nj]==1:
            Q += [(ni,nj)]
            arr[ni][nj] = arr[i][j] + 1

print(arr[-1][-1]) 