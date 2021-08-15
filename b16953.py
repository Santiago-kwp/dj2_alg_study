'''
연산 종류 
1. 2를 곱한다 = A * 2
2. 1을 수 가장 오른쪽에 추가한다. = A * 10 + 1
경우의 수가 2이므로 한번 연산 시마다 2**N 의 경우의 수가 생김 -> 모든 경우의 수를 보는건 비효율적
접근 방식 : 그리디 알고리즘으로 한번에 크게 줄일 수 있는 2번연산 우선시
B의 첫째자리 값이 1이면 
B의 첫째자리 값이 1이 아닌 홀수면 -1 반환
B가 짝수면 2로 나눔 --> 반복
'''
A, B = map(int,input().split())
cnt = 0
while(A<B):
    if B%10 == 1:
        B = (B-1)//10
        cnt += 1
    elif B%2:
        cnt = -2
        break
    else: 
        B = B//2
        cnt += 1

print(cnt+1 if A==B else -1)

