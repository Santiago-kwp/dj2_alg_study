# ㅈ 모양은 한 정점에서 인접한 다른 정점이 3개 이상이면 3개 이상의 정점 중 3개씩 뽑는 조합의 수
# ㄷ 모양은 한 정점에서 인접한 정점이 2개 이상이고, 다음 인접한 정점의 인접한 정점이 2개 이상일 때 (두 인접한 정점의 수-1) 끼리의 곱...
# 예를들어 1 - 2 - 3 - 4 - (5, 6) 이면 2번 정점은 1, 3이 인접한 정점이고, 3은 2, 4가 인접한 정점이므로 (2-1)*(2-1) = 1개의 경우의 수

import sys
N = int(input())
adj = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

dcnt = jcnt = 0
Q = [1]
visit[1] = 1
for x in Q:
    n = len(adj[x])
    if n > 2:
        jcnt += n*(n-1)*(n-2)//6
    for v in adj[x]:
        if not visit[v]:
            visit[v] = 1
            Q.append(v)
            if n>1 and len(adj[v]) > 1:
                dcnt += (n-1)*(len(adj[v])-1)    
            
ans = 'D'
if dcnt == 3*jcnt: ans = 'DUDUDUNGA'
if dcnt < 3*jcnt: ans = 'G'
print(ans)

# for loop 완전탐색
# for i in range(1, N+1):
#     n = len(adj[i])
#     if n < 2: continue
#     if n > 2:
#         jcnt += n*(n-1)*(n-2)//6
#     for v in adj[i]:
#         if v < i: continue  # visited 처리 
#         if n>1 and len(adj[v]) > 1:
#             dcnt += (n-1)*(len(adj[v])-1)     

# BFS 10%에서 틀렸습니다...는 DUDUDUNGA 인데 DUDUNGA 만씀...
# Q = [1]
# visit[1] = 1
# for x in Q:
#     n = len(adj[x])
#     if n > 2:
#         jcnt += n*(n-1)*(n-2)//6
#     for v in adj[x]:
#         if n>1 and len(adj[v]) > 1:
#             dcnt += (n-1)*(len(adj[v])-1)    
#         if not visit[v]:
#             visit[v] = 1
#             Q.append(v)

# DFS 10% 에서 틀렸습니다..
# sys.setrecursionlimit(10**8)
# def dfs(x):
#     global dcnt, jcnt
#     n = len(adj[x])
#     if n > 2:
#         jcnt += n*(n-1)*(n-2)//6
#     for v in adj[x]:
#         if not visit[v]:
#             if n > 1 and len(adj[v]) > 1:
#                 dcnt += (n-1) * (len(adj[v])-1)
#             visit[v] = 1
#             dfs(v)
