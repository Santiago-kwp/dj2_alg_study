'''
W/(단말 노드의 개수?!)
단말 노드 = 한번만 방문된 노드, 
루트(= 1번인덱스)를 빼고 계산하는게 핵심
1 -> 2 -> 3 -> 5,6 인 경우 한번 방문 노드 1, 5, 6 이 되버림
'''
import sys
N, W = map(int, input().split())
visit = [0]*(N+1)
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    visit[U] += 1
    visit[V] += 1
print(W/visit[2:].count(1))



'''
스택을 통해 dfs 구현했으나 시간 초과...
''' 
# import sys
# N, W = map(int, input().split())
# visit = [0]*(N-1)
# tree = []
# for _ in range(N-1):
#     tree.append(list(map(int, sys.stdin.readline().split())))
# q = [1]
# cnt = 1
# while q:
#     t = q.pop()
#     for j in range(N-1):
#         if not visit[j]:
#             if tree[j][0] == t:
#                 visit[j] = 1
#                 q.append(j)
#             elif tree[j][1] == t:
#                 visit[j] = 1
#                 q.append(j)
#             else:
#                 cnt+= 1
# print(W/cnt)
'''
재귀로 단말 노드 개수를 구현했으나 시간 초과...
'''
# cnt = 1
# def find_term(i):
#     global cnt
#     for j in range(N-1):
#         if not visit[j] and tree[j][0] == i: 
#             i = tree[j][1]
#             visit[j] = 1
#             find_term(i)
#         if not visit[j] and tree[j][1] == i:
#             i = tree[j][0]
#             visit[j] = 1
#             find_term(i)
#     cnt+=1
        
# find_term(1)
# print(W/cnt)
