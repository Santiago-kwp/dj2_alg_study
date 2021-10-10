
def BFS():
    # 시작점 정의 (벽 부술 수 있는 경우 1 / 없으면 0, i, j)
    Q = [(1, 0, 0)]
    visited[1][0][0] = 1
    for f, i, j in Q:
        # 도착한 경우 해당 지점의 거리 반환
        if (i, j) == (N-1, M-1):
            return visited[f][i][j]

        # 4방향 탐색
        for k in range(4):
            ni, nj = i+d[k], j+d[k-2]
            # 지도 밖인 경우
            if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
            # 미방문한 곳 중에
            if not visited[f][ni][nj]:
                # 값이 0이어서 그냥 갈 수 있는 경우
                if not arr[ni][nj]:
                    visited[f][ni][nj] = visited[f][i][j] + 1
                    Q.append((f, ni, nj))
                # 값이 1이라 갈 수 없지만 부술 수 있는 경우
                if arr[ni][nj] and f:
                    visited[0][ni][nj] = visited[f][i][j] + 1
                    Q.append((0, ni, nj))
    return -1

# 방향 설정
d = [0, 0, -1, 1]   
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 3차원 visited 정의 1차원 벽 부순 경우 O // X, 2, 3차원 = r, c
visited = [[[0]*M for _ in range(N)] for _ in range(2)]

print(BFS())



### DFS 활용 시 메모리 초과 발생...
# d = [0, 0, -1, 1]
# def DFS(i, j , m, flag):
#     global min_move
#     if m >= min_move: return
#     if (i, j) == (N-1, M-1):
#         min_move = min(m, min_move)
#         return
#     arr[i][j] = 1
#     for k in range(4):
#         ni, nj = i+d[k], j+d[k-2]
#         if 0<=ni<N and 0<=nj<M:
#             if not arr[ni][nj]:
#                 DFS(ni, nj, m+1, flag)
#             elif arr[ni][nj] and flag:
#                 DFS(ni, nj, m+1, 0)
#                 arr[ni][nj] = 1
#     arr[i][j] = 0
    
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# min_move = N*M+1
# DFS(0, 0, 1, 1)
# print(min_move if min_move != N*M+1 else -1)