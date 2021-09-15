'''
이진트리의 자식노드가 2*k, 2*k+1임을 이용하여
한 노드가 들어왔을 때 그 노드와 자식노드 전체를
재귀를 통해 방문 처리하여 다음 노드가 들어왔을 때
방문 여부 점검하여 한번에 방문 안했으면 0, 
방문한 경우 방문 안한 부모노드를 찾아 프린트함
'''
import sys
N, Q = map(int, input().split())
visited = [0]*(N+1)
def tree(i):
    if i > N:
        return
    else:
        visited[i] = 1
        tree(2*i)
        tree(2*i+1)
    
for _ in range(Q):
    i = int(sys.stdin.readline())
    if not visited[i]:
        print(0)
        tree(i)
    else:
        while visited[i//2]:
            i //= 2
        print(i)