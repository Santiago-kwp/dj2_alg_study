# 아래 코멘트 처리된 코드를 중복 배제하여 줄인 코드
N, M = map(int, input().split())
Rs = [0]+[int(input()) for _ in range(N)]   
Wk = [0]+[int(input()) for _ in range(M)]   
earn = 0
park = [0]*(N+1)
wait = []
for _ in range(2*M):
    c = int(input())
    if c>0:
        if park.count(0) > 1:
            i = 1
            while park[i]:
                i += 1
            park[i] = c
        else:
            wait.append(c)
    else:
        idx = park.index(-c)
        earn += Rs[idx]*Wk[-c]
        if wait:
            park[idx] = wait.pop(0)
        else:
            park[idx] = 0
print(earn)


# 아래는 조건에 맞게 무지성 일단 구현 코드

# N = 주차 공간 수, M = 차량의 수 
# N, M = map(int, input().split())
# Rs = [0]+[int(input()) for _ in range(N)]   # 주차공간 당 요금
# Wk = [0]+[int(input()) for _ in range(M)]   # 1~M 번까지 차의 무게

# earn = 0
# order = []
# for i in range(2*M):
#     order.append(int(input()))
# park = [0]*(N+1)                # 주차장 공간
# wait = []                       # 주차장이 꽉찬 경우의 대기조
# while order:
#     c = order.pop(0)            # 순서에서 맨 앞에 하나 빼서
#     if c>0 and park.count(0) > 1:    # 주차장에 빈 공간이 있는 경우
#         i = 1
#         while park[i]:          # 주차장의 앞부터 공간 있는지 확인
#             i += 1
#         park[i] = c             # 공간이 있으면 해당 공간에 차 넣기

#     elif c>0 and park.count(0) == 1:    # 차가 들어오려는데 주차장이 꽉찬 경우
#         wait.append(c)                  # 해당 차를 대기열에 넣기

#     if c<0:                     # 차를 빼려는 경우
#         idx = park.index(-c)     # 해당 차가 주차된 인덱스를 찾고
#         earn += Rs[idx]*Wk[-c]   # 수금을 하고

#         if wait:                # 기다리는 차가 있는 경우
#             park[idx] = wait.pop(0)
#         else:
#             park[idx] = 0       # 차를 뺀다


# print(earn)