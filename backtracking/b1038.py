'''
BFS느낌으로 큐에 0~9까지 넣은 후에 1부터 하나씩 빼고, 뺀수의 마지막 자리수 (q[-1])
보다 작은 수를 string concatenate 하여 큐에 enqueue 하는 방식
'''
N = int(input())
# 0 ~ 9까지 큐에 넣기
Q = list(map(str, range(10)))
# BFS 
for n, q in enumerate(Q):
    if n == N:              # 인덱스가 해당 N 번째 수일 경우 그 때의 숫자 q를 출력하고 루프문 나감
        print(q)
        break
    for i in range(int(q[-1])): # 마지막 자리수보다 작은 수를 더해서 큐에 enqueue
        Q.append(q+str(i))
else:                       # 큐가 비어서 끝났는데 못찾으면 -1 프린트
    print(-1)