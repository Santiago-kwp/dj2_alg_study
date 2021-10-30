'''
문자열 딕셔너리화해서 개수 세기
'''
N, M = map(int, input().split())
S = {}
for _ in range(N):
    S[input()] = 1

cnt = 0
for i in range(M):
    try: 
        S[input()] += 1
        cnt += 1
    except: continue

print(cnt)