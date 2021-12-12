# Pypy3으로만 됨. Python 시간초과...
# 연결 요소의 개수
# N: 정점의 개수, M: 간선의 개수
N, M = map(int, input().split())

# 인접 행렬 정의
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# 연결 요소의 개수
cnt = 0
visited = [0]*(N+1)
# 모든 노드 BFS로 확인
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        Q = [i]
        for j in Q:
            for k in adj[j]:
                if not visited[k]:
                    visited[k] = 1
                    Q.append(k)
        cnt += 1

print(cnt)







