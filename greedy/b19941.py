# 햄버거 분배
# N: 식탁의 길이, K: 햄버거를 선택할 수 있는 거리
'''
사람(P)의 위치를 기준으로 -K ~ +K 거리 안에 햄버거(H)가 있는 경우에 
우선 순위( -K 최우선 + K 최하위 )를 두고 고르고 그 햄버거를 X 표시해서 먹은걸로 하자
'''
N, K = map(int, input().split())
location = list(input())
# 먹은 사람의 수
cnt = 0
for i, a in enumerate(location):
    if a == 'P':
        si = max(0, i-K)
        ei = min(N, i+K+1)
        for j in range(si, ei):
            if location[j] == 'H':
                location[j] = 'X'
                cnt += 1
                break

print(cnt)


# 최적의 햄버거를 찾는 레이더 함수-> 같은 결과
# def radar(pidx):
#     global cnt
#     si = max(0, pidx-K)
#     ei = min(N, pidx+K+1)
#     for i,a in enumerate(location[si:ei], start=si):
#         if a == 'H':
#             location[i] = 'X'
#             cnt += 1
#             return

# for i, a in enumerate(location):
#     if a == 'P':
#         radar(i)
#         print(location)







