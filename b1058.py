'''
2-친구: 각 노드별 간선이 2개까지로 연결된 접점의 수 
bfs로 접근하여 각 노드의 간선의 길이가 2,3 인 정점의 개수 중 최댓값
'''
N = int(input())
adj = [input() for _ in range(N)]
maxc = 0
for i in range(N):
    visited = [0]*N
    cnt = 0
    q = [i]
    visited[i] = 1
    while q:
        t = q.pop(0)
        for w in range(N):
            if adj[t][w] == 'Y' and not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1
    for v in visited:
        if 1< v < 4:
            cnt += 1
    if maxc < cnt:
        maxc = cnt
print(maxc)    
