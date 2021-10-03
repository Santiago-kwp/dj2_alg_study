N = int(input())
col = []
for _ in range(N):
    L, H = map(int, input().split())
    col.append([L, L+1, H])
# 기둥 위치를 기준으로 정렬
col.sort()
maxw = col[-1][1] - col[0][0]

# 왼쪽에서 오른쪽으로 가면서 maxh를 갱신하면서 계산
area = 0
h =  col[0][2]
for i in range(len(col)-1):
    w = col[i+1][0] - col[i][0]
    area += w*h
    h = max(col[i+1][2], h)
    # if col[i+1][2] > h:
    #     h = col[i+1][2]

# 오른쪽에서 왼쪽으로 가면서 maxh를 갱신하면서 계산
h = col[-1][2]
# 처음 시작시
for i in range(len(col)-1,0,-1):
    w = col[i][1] - col[i-1][1]
    area += w*h
    h = max(col[i-1][2], h)
    
# 양끝점 추가
area += 2*h

print(area-maxw*h)