'''
b1068 숏코딩 복기코드, 재귀룰 사용하지 않고, while문을 통해 부모노드를 탐색하면서
구현한 코드
'''
N = int(input())
parent = list(map(int, input().split()))
r = int(input())
# 활성화된 노드는 1, 아니면 0
nodes = [1]*N

# 삭제할 노드 비활성화 
parent[r] = -2
# 한 노드씩 순회하면서 부모노드를 찾음
for i in range(N):
    x = i
    while x>=0: # 부모 노드가 루트이거나 삭제된 노드일 경우 멈춤
        x = parent[x] 
    if x == -2: # 부모 노드가 삭제된 노드일 경우
        nodes[i] = 0 # 그 노드는 비활성화
    elif parent[i] != -1:   # 현재 노드의 부모가 루트노드가 아닐 경우
        nodes[parent[i]] = 0    # 부모 노드는 단말 노드에서 제외

print(sum(nodes))