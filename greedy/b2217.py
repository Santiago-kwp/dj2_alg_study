'''
줄이 3개면 -> 
3개 중 3번째 큰 중량 줄 *3 or 3개중 2번째 큰 중량 줄 *2 
or 3개중 1번째 큰 중량 줄 *1
'''
N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()
max_weight = 0
for i in range(1,N+1):
    if max_weight < ropes[-i]*i:
        max_weight = ropes[-i]*i
print(max_weight)