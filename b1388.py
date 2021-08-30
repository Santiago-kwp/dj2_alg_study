N, M = map(int, input().split())
flat = [input()+'0' for _ in range(N)]  #행, 열 '0' 패딩 추가
flat.append('0'*(M+1))
cnt = 0
for i in range(N):      # 가로 검사
    j = 0
    while(j < M):
        if flat[i][j] == '-':
            if flat[i][j+1] != '-':
                cnt += 1
        j += 1
for j in range(M):      # 세로 검사
    i = 0
    while(i < N):
        if flat[i][j] == '|':
            if flat[i+1][j] != '|':
                cnt += 1
        i += 1
print(cnt)
        
            



                
        