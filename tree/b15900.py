# 처음 시작 : 트리의 모든 리프 노드에 게임말이 하나씩 놓여있는 채로 시작
# 차례 : 현재 존재하는 게임말 중 아무거나 하나를 골라 그 말이 놓여 있던 노드의 부모 노드로 옮긴다.
# 이동 과정에서 한 노드에 여러 개의 게임말이 놓이게 될 수 있음
# 옮긴 후 만약 게임말이 루트 노드에 도착했다면 그 게임말을 즉시 제거
# 승리 조건 : 게임말이 게임판에 존재하지 않아 고를 수 없는 사람이 지게 됨
# 즉 마지막에 하나 남은 게임말을 루트 노드에 안착 시키면 다음 사람이 패배

# 선 플레이어 승리 조건: 모든 리프 노드 -> 루트 노드까지 이동하는 간선 숫자의 합이 홀수면 ?!
# 루트 노드에서 모든 리프 노드까지 이동한 거리의 합이 홀수면 됨!
# Root -> bottom (top-down) 방식은 시간 초과...
import sys
sys.setrecursionlimit(10**9)
def find_leaf(x, n):
    global cnt
    if x!=1 and len(adj[x]) == 1:
        cnt += n
    else:
        for v in adj[x]:
            if not visit[v]:
                visit[v] = 1
                find_leaf(v,n+1)

N = int(input())
p = list(range(1, N+1))
adj = [[] for _ in range(N+1)]
visit = [1]+[0]*(N)
cnt = 0
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
find_leaf(1,0)
print('Yes' if cnt%2 else 'No')
