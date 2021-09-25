# 선형 큐 활용
# 큐가 버퍼 크기만큼 찼다는 것은 rear-front == N
import sys

N = int(input())
Q = [0]*(N+100001)
front = rear = -1
while (a:=int(sys.stdin.readline())) != -1:
    if a: 
        if rear-front<N:
            rear += 1
            Q[rear] = a
        else:
            continue
    else:
        front += 1
if front != rear:
    print(*Q[front+1:rear+1])
else:
    print('empty')
    




