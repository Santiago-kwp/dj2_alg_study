'''
무지성 모든 노드에서 다 시작하면서 방문 노드의 수 세고
최대값 찾아서 프린트
'''
import sys
def bfs(Q, h):
    for b in Q:
        for a in trust[b]:
            if not visited[a]:
                visited[a] = 1
                h += 1
                Q.append(a)
    return h

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    trust[B].append(A)
maxh = 0
hlist = [0]*(1+N)
for b in range(1, N+1):
    if trust[b]:
        visited = [0]*(1+N)
        visited[b] = 1
        h = bfs([b], 0)
        hlist[b] = h
        maxh = max(maxh, h)

for b in range(1, N+1):
    if hlist[b] == maxh:
        print(b, end=' ')