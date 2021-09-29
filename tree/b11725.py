# 각 노드의 부모를 구하는 프로그램
# 간선의 정보를 2d list 로 저장하여 루트 노드부터 자식 노드로 방문하면서
# 부모가 정해지지 않은 경우만 재귀 호출함
# 재귀 한계선이 넘어가는 경우가 생겨 임의로 늘려줘야됬던 문제..
import sys
sys.setrecursionlimit(10**9)

def dfs(p):
    for v in edge[p]:
        if not parent[v]:
            parent[v] = p
            dfs(v)

N = int(input())
edge = [[]*(N+1) for _ in range(N+1)]
parent = [0]*(N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
dfs(1)

for p in parent[2:]:
    print(p)


# 단말 노드를 큐에 넣고 하나씩 비교하는 무지성 코드.. 시간 초과
# import sys
# N = int(input()) 
# cnt = [0]*(N+1)
# visited = [0]*(N-1)
# edge = []
# for _ in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     cnt[a] += 1
#     cnt[b] += 1
#     edge.append([a,b])

# Q = []
# for idx, i in enumerate(cnt[2:], start=2):
#     if i == 1:
#         Q.append(idx)

# parents = [0]*(N+1)
# for v in Q:
#     for i in range(N-1):
#         a, b = edge[i]
#         if not visited[i]:
#             if v == 1:
#                 visited[i] = 1
#                 if a == 1:
#                     parents[b] = 1
#                 if b == 1:
#                     parents[a] = 1
#             elif v == a:
#                 parents[v] = b
#                 Q.append(b)
#                 visited[i] = 1
#             elif v == b:
#                 parents[v] = a
#                 Q.append(a)
#                 visited[i] = 1

# for p in parents[2:]:
#     print(p)

