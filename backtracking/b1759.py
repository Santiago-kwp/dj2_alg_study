# C개의 문자 중 모음을 뽑는 수는 1, 2, ... 최대 C-2개까지 
# 전체 경우의 수 중 모음의 개수가 1~L-2일 때 출력
L, C = map(int, input().split())
Cstr = sorted(list(input().split()))
vowel = ['a','i','e','o','u']

v = [0]*C
def dfs(idx, cnt):
    if cnt == L:
        com = ''
        vcnt = 0
        for i in range(C):
            if v[i]:
                com+=Cstr[i]
                if Cstr[i] in vowel:
                    vcnt += 1
        if 0 < vcnt < L-1:
            print(com)
        return
    else:
        for i in range(idx,C):
            if v[i]:
                continue
            else:
                v[i] = 1
            dfs(i, cnt+1)
            v[i] = 0
dfs(0,0)

