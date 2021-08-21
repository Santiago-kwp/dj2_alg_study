'''
A, B, C로 된 3개의 하노이 봉을 스택으로 보고
A에서 하나씩 빼서 N 이면 C로 넣고 아니면 B로 넣기
flag 변수를 이용하여 A를 다 돈 후 B를 돌고
다시 B를 다 돌면 A를 도는 식으로 최적화
'''
N = int(input())
A = list(map(int,input().split()))
B = []
C = []
P = []
cnt = 0
flag = 1
while(N > 0):
    if flag:
        while(A):
            if A[-1] == N:
                C.append(A.pop())
                N -= 1
                P.append('1 3')
                cnt += 1
            else:
                B.append(A.pop())
                P.append('1 2')
                cnt += 1
        flag = 0
    else:
        while(B):
            if B[-1] == N:
                C.append(B.pop())
                N -= 1
                P.append('2 3')
                cnt += 1
            else:
                A.append(B.pop())
                P.append('2 1')
                cnt += 1
        flag = 1

print(cnt)
for i in range(len(P)):
    print(P[i])




