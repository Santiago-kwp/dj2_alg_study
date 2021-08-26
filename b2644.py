'''
front, rear를 통해 queue 구현
queue 를 이용한 BFS 구현 간 간선 거리 visited[w] = visited[i] +1 갱신
'''
n = int(input())
S, G = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

q = [0]*101
visited = [0]*(n+1)
front, rear, cnt = -1, 0, 0
q[rear] = S

while front != rear:
    front += 1
    i = q[front]
    for w in adj[i]:
        if not visited[w]:
            visited[w] = visited[i] + 1
            rear += 1
            q[rear] = w
            if w == G:
                cnt = visited[w]

print(cnt if cnt else -1)





