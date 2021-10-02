N = int(input())
B = list(map(int, input().split()))
# A를 B로 만들어주기위한 연산의 최소 횟수
# B를 A로 만들어주기
cnt = -1
while 1:
    # 1. 모든 원소를 짝수로 만들어주기
    for b in B:
        # 각 원소가 홀수면
        if b%2:
            cnt += 1
            b -= 1
    # 2. 모든 원소를 2로 나눠주기
    B = [b//2 for b in B]
    cnt += 1
    if B == [0]*N:
        break
print(cnt)
