'''
bfs로 최단거리 찾기
'''
def bfs(n, t):
    Q = [(n, t)]
    visited[n] = 1
    if n >= K: return n-K
    for n, t in Q:
        if n <0 or n > K+1: continue
        if n == K: 
            return t
        cho = [n-1, n+1, 2*n]
        for i in range(3):
            if not visited[cho[i]]:
                visited[cho[i]] = 1
                Q += [(cho[i], t+1)]

N, K = map(int, input().split())
visited = [0]*200001
print(bfs(N,0))

# def bfs(n, t):
#     Q = [(n, t)]
#     visited[n] = 1
#     for n, t in Q:
#         if n == K: 
#             return t
#         for nn in [n-1, n+1, 2*n]:
#             if 0<=nn and nn<=BIG and not visited[nn]:
#                 visited[nn] = 1
#                 Q += [(nn, t+1)]

# N, K = map(int, input().split())
# BIG = 200000
# visited = [0]*(BIG+1)
# print(bfs(N,0))
