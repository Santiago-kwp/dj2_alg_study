# 지름길
# N: 지름길의 개수, D: 고속도로의 길이
N, D = map(int,input().split())
road = []
for _ in range(N):
    s, e, w = map(int, input().split())
    road.append((s, e, w))

# 시작 지점을 기준으로 오름차순 정렬
road.sort()

oil_road = list(range(D+1))

for s, e, w in road:
    # 도착 지점이 D 이하이고, 현재 저장된 지름길보다 짧아야 됨
    if e <= D and oil_road[e] > oil_road[s] + w:
        # 모든 지점마다 작은 쪽으로 비교하여 지름길 갱신
        oil_road[e:] = [min(x,y) for x,y in zip(range(oil_road[s]+w, oil_road[s]+w + D-e + 1), oil_road[e:])]

print(oil_road[-1])



'''
for s, e, w in road:
    # 도착 지점이 D 이하이고, 현재 저장된 지름길보다 짧아야 됨
    if e <= D and oil_road[e] > oil_road[s] + w:
        # 지름길 갱신
        oil_road[e:] = list(range(oil_road[s]+w, oil_road[s]+w + D-e + 1))

print(oil_road[-1])
'''
'''
위와 같이 갱신하면 예외 케이스 존재...
6 150
0 50 10
0 45 0
0 149 3
50 100 10
100 151 10
110 140 90
'''

'''
코드 줄여보기
N, D = map(int,input().split())
road = sorted([list(map(int, input().split())) for _ in range(N)])
oil = list(range(D+1))
for s, e, w in road:
    if e <= D and oil[e] > oil[s] + w:
        oil[e:] = [min(x,y) for x,y in zip(range(oil[s]+w, oil[s]+w + D-e + 1), oil[e:])]
print(oil[-1])
'''
