'''
스택을 이용한 DFS 구현, 인접 리스트 사용
'''
V, E = int(input()), int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

visited = [0]*(V+1)
stack = [1]
cnt = 0
while stack:
    i = stack.pop()
    visited[i] = 1
    for w in adj[i]:
        if not visited[w]:
            stack.append(w)
            visited[w] = 1
            cnt += 1
print(cnt)
    

